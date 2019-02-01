
import matplotlib.pyplot as plt

def plot(apex_data, title, xdata, xlabel, ydata, ylabel):
    plt.plot(apex_data[xdata], apex_data[[ydata]])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()