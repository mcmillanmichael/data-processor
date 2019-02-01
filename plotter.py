
import generic.plotter as plt

global show_plots
show_plots = True

def plot_arrival_delay(apex_data, title, xlabel, ylabel):
    plot(apex_data, title, 'onchocks', xlabel, 'arrival_delay', ylabel)

def plot_departure_delay(apex_data, title, xlabel, ylabel):
    plot(apex_data, title, 'offchocks', xlabel, 'departure_delay', ylabel)

def plot(apex_data, title, xdata, xlabel, ydata, ylabel):
    if show_plots:
        plt.plot(apex_data, title, xdata, xlabel, ydata, ylabel)