USE UltraAIMS_JNB
go

declare @max_date datetime2 = (select max(ScheduledToArrive) from FlightsLive.FlightLeg)
declare @min_date datetime2 = dateadd(year, -3, @max_date)


select x.*
from
(
	select 
		v.VisitId,

		ac.Registration 'aircraft_reg', act.IcaoType 'aircraft_icao_type', act.Width 'aicraft_width', act.Length 'aircraft_length',

		ifl.ScheduledArrivalTime 'sched_arrival', ifl.FlightNumber 'arrival_fln', ar.Name 'arrival_runway', ast.Name 'arrival_stand',
		(select count(1) from ResourcesLive.GateAllocation ga where ga.VisitId = v.visitid and ga.IsForArrival = 1) 'arrival_gate_count',

		ofl.ScheduledDepartureTime 'sched_departure', ofl.FlightNumber 'dep_fln', dr.Name 'dep_runway', dst.Name 'dep_stand', dsa.OrderNumber 'number_of_stands',
		(select count(1) from ResourcesLive.GateAllocation ga where ga.VisitId = v.visitid and ga.IsForArrival = 0) 'departure_gate_count',
		(select count(1) from ResourcesLive.GateAllocation ga where ga.VisitId = v.visitid and ga.IsForArrival = 0) 'departure_staff_gate_count',

		m6.Scheduled 'sched_landed', m6.Actual 'landed', m7.Scheduled 'sched_onchocks', m7.Actual 'onchocks', 
		m15.Scheduled 'sched_offchocks', m15.Actual 'offchocks', m16.Scheduled 'sched_takeoff', m16.Actual 'takeoff',
		DATEDIFF(minute, m7.Scheduled, m7.Actual) 'arrival_delay',
		DATEDIFF(minute, m15.Scheduled, m15.Actual) 'departure_delay',
	
		oa.IcaoCode 'airport_origin', fa.IcaoCode 'airport_from', a.IcaoCode 'airport_current', ta.IcaoCode 'airport_to',
		iairline.IataCode 'arrival_airline', oairline.IataCode 'departure_airline'


	from flightslive.visit v

	--flights
	join flightslive.FlightLeg ifl on ifl.FlightLegId = v.InboundFlightLegId
	join flightslive.FlightLeg ofl on ofl.FlightLegId = v.OutboundFlightLegId
	join ResourcesLive.Runway ar on ar.RunwayId = ifl.ArrivalRunwayId
	join ResourcesLive.Runway dr on dr.RunwayId = ofl.DepartureRunwayId

	--aircraft
	join AircraftLive.Aircraft ac on ac.AircraftId = v.AircraftId
	join AircraftLive.AircraftType act on act.AircraftTypeId = ac.AircraftTypeId

	--airports
	join OrganisationsLive.Airport oa on oa.AirportId = ifl.OriginAirportId
	join OrganisationsLive.Airport fa on fa.AirportId = ifl.DepartureAirportId
	join OrganisationsLive.Airport a on a.AirportId = v.AirportId
	join OrganisationsLive.Airport ta on ta.AirportId = ofl.ArrivalAirportId

	--airline
	join OrganisationsLive.Airline iairline on iairline.AirlineId = ifl.AirlineId
	join OrganisationsLive.Airline oairline on oairline.AirlineId = ofl.AirlineId

	--codeshares
	--join FlightsLive.FlightLegCodeShare iflcs on iflcs.FlightLegId = ifl.FlightLegId
	--join FlightsLive.FlightLegCodeShare oflcs on oflcs.FlightLegId = ofl.FlightLegId

	--first stand
	join ResourcesLive.StandAllocation asa on asa.VisitId = v.VisitId and asa.OrderNumber = 1
	join ResourcesLive.Stand ast on ast.StandId = asa.StandId

	--last stand
	join ResourcesLive.StandAllocation dsa on dsa.VisitId = v.VisitId and dsa.OrderNumber = (select max(OrderNumber) from ResourcesLive.StandAllocation where VisitId = v.VisitId)
	join ResourcesLive.Stand dst on dst.StandId = dsa.StandId

	--landed\inblocks\offblocks\takeoff milestones
	join FlightsLive.Milestone m6 on m6.VisitId = v.VisitId and m6.MilestoneTypeId = 6 and m6.Actual is not null
	join FlightsLive.Milestone m7 on m7.VisitId = v.VisitId and m7.MilestoneTypeId = 7 and m7.Actual is not null
	join FlightsLive.Milestone m15 on m15.VisitId = v.VisitId and m15.MilestoneTypeId = 15 and m15.Actual is not null 
	join FlightsLive.Milestone m16 on m16.VisitId = v.VisitId and m16.MilestoneTypeId = 16 and m16.Actual is not null

	where (ifl.ScheduledToArrive > @min_date or ofl.ScheduledToDepart > @min_date)
) x
where x.arrival_delay is not null and x.departure_delay is not null
and x.arrival_delay between -800 and 50000
and x.departure_delay between -800 and 50000
order by x.sched_arrival, x.sched_departure
--order by x.departure_delay