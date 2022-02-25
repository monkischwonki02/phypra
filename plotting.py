import matplotlib.pyplot as plt
import numpy as np

'''
# creates a plot with errorbars
#
# parameters:
# x,y - np.ndarray (n,) : data
# err - np.ndarray (n,) : error of y
# head : title of diagram
# xlbl : Label of x-Axis
# ylbl : label of y-Axis
# cl: color of graph (see on https://matplotlib.org/stable/gallery/color/named_colors.html)
#
# return:
# returns matplotlib.figure.Figure Object 
'''
def plot_err(x: np.ndarray,y: np.ndarray,err: np.ndarray, head="", xlbl="", ylbl="", cl=""):
    fig, ax1 = plt.subplots(1)

    ax1.errorbar(x,y,err, color=cl)
    ax1.grid()
    ax1.set(xlabel=str(xlbl), ylabel=str(ylbl))
    fig.suptitle(str(head))
    ax1.scatter(x,y,color=cl)

    return fig


'''
# creates a plot with 'm'-Graphs
# 
# parameters:
# x,y  - np.ndarray (n,m) : n lists with m-datapoints
# err - np.ndarray (n,m) : errors of data
# head : title of diagram
# xlbl : Label of x-Axis
# ylbl : label of y-Axis
# legend: names of every single graph
# cl: color of graph (see on https://matplotlib.org/stable/gallery/color/named_colors.html)
#
# return:
# returns matplotlib.figure.Figure Object 
'''
def plot_err_mul(x: np.ndarray,y: np.ndarray,err: np.ndarray, head="", xlbl="", ylbl="", legend=[], cl=[]):
    fig, ax1 = plt.subplots(1)
    for i in range(x.shape[0]):
        if len(legend) <= x.shape[0]:
            for _ in range(x.shape[0] - len(legend)):
                legend.append("")
        ax1.errorbar(x[i, :], y[i, :], err[i, :], label=legend[i], c=cl[i])
        ax1.scatter(x[i,:], y[i,:], c=cl[i])
    ax1.grid()
    ax1.set(xlabel=str(xlbl), ylabel=str(ylbl))
    ax1.legend()
    fig.suptitle(str(head))
    return fig

