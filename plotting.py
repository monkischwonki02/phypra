import matplotlib.pyplot as plt
import numpy as np


'''
# creates a errorbar-plot with 'n'-Graphs
# 
# args:
# x,y  - np.ndarray (n,m) : n lists with m-datapoints
# err - np.ndarray (n,m) : errors of data
# head : title of diagram
# xlbl : Label of x-Axis
# ylbl : label of y-Axis
# legend: names of every single graph
# cl: color of graphs (see on https://matplotlib.org/stable/gallery/color/named_colors.html)
#
# return:
# returns matplotlib.figure.Figure Object 
'''
def plot_err(x: np.ndarray,y: np.ndarray,err: np.ndarray, head="", xlbl="", ylbl="", legend=[], cl=[]):
    fig, ax1 = plt.subplots(1)
    for i in range(x.shape[0]):
        if len(legend) <= x.shape[0]:
            for _ in range(x.shape[0] - len(legend)):
                legend.append("")
        ax1.errorbar(x[i, :], y[i, :], err[i, :], label=legend[i], c=cl[i])
        ax1.scatter(x[i, :], y[i, :], c=cl[i])
    ax1.grid()
    ax1.set(xlabel=str(xlbl), ylabel=str(ylbl))
    ax1.legend()
    fig.suptitle(str(head))
    return fig

'''
# plots multiple graphs (n "lines")
# 
# args:
# x,y - np.ndarray (n,m): n lists with m datapoints
# xlbl, ylbl : label of x and y-axis
# legend : short description of every graph
# color : color for every graph
#
# returns:
# plt.Figure object
'''
def plot_lin(x: np.ndarray, y: np.ndarray, head = "", xlbl = "", ylbl = "", legend = [], color=[]):
    fig, ax1 = plt.subplots(1)

    if len(x.shape) == 2:
        for i in range(x.shape[0]):
            if len(legend)<=x.shape[0]:
                for _ in range(x.shape[0] - len(legend)):
                    legend.append("")
            if len(color) <= x.shape[0]:
                for _ in range(x.shape[0]- len(color)):
                    color.append(None)
            ax1.plot(x[i, :], y[i, :], label=legend[i], c=color[i])
            ax1.scatter(x[i, :], y[i, :], c=color[i])
    else:
        if len(legend) == 0:
            legend.append("")
        if len(color) == 0:
            color.append(None)
        ax1.plot(x, y, c=color[0])
        ax1.scatter(x,y,c=color[0])
    ax1.grid()
    ax1.set(xlabel=xlbl, ylabel=ylbl)
    return fig


'''
# saves the plot as an image
#
# args:
# fig (plt.Figure) : matplotlib figure with plot
# path : path where the function saves the plot
# name : name of image
'''
def save_plot(fig: plt.Figure, path: str, name: str, f: str):
    fig.savefig(path + name + "." + f, format=f)