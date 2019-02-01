import sys

# make the /generic/ directory available for imports.
sys.path.insert(0, './generic/')

import config
import plotter
import generic.output as o
import loader
import features

####################

# declare vars
apex_data = None
feature_manager = None

# configure vars
plotter.show_plots = False
o.output_verbose = False
o.output_information = True

def main():
    try:
        # read config file
        feature_manager = features.FeatureManager()
        c = config.ConfigManager('config.json', feature_manager)

        # load apex data, relative to current directory
        apex_data = loader.load(c.data_file, feature_manager, process_data=True)

        # plot the delay data
        #plotter.plot_arrival_delay(apex_data, 'arrival_delay data shape', 'onchocks', 'arrival delay mins')
        #plotter.plot_departure_delay(apex_data, 'departure_delay data shape', 'offchocks', 'departure delay mins')

        # write the data back to CSV so we can easily see it
        o.print_info('outputting transformed data to: {}'.format(c.output_data_file))
        apex_data.to_csv(c.output_data_file)

    except Exception as ex:
        o.print_error(ex)


main()