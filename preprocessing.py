import numpy as np


'''
# split the data in x and y 
#
# args:
# data - np.ndarray: raw data
# x_rows : list with rows, that are associated with x
# y_rows : list with rows, that are associated with y
#
# returns:
# x , y - np.ndarray
'''
def split_data(data: np.ndarray, x_rows: list, y_rows: list):
    x = np.array([])
    y = np.array([])
    for x_row in x_rows:
        x = np.concatenate((x,data[x_row, :]))
    for y_row in y_rows:
        y = np.concatenate((x, data[y_row, :]))

    return (x,y)


'''
# transforms 1D-Coordinates with a defined transformation
#
# args:
# x - np.ndarray (n,): coordinates to be transformed
# transform - function (lambda) : function to transform coordinates 
#
# return transformed coordinates
'''
def transform_1d(x: np.ndarray, transform):
    return transform(x)

'''
# transforms 2D-Coordinates with a defined transformation
#
# args:
# x - np.ndarray (n,): coordinates to be transformed
# y - np.ndarray (n,): coordinates to be transformed
# transform - function (lambda) : function to transform coordinates 
#
# return:
# tupel with the transformed coordinates (x_t, y_t)
# x_t - np.ndarray (n,) : transformed coordinates
# y_t - np.ndarray (n,) : transformed coordinates
'''
def transform_2d(x: np.ndarray, y: np.ndarray, transform):
    x_t = transform(x)
    y_t = transform(y)
    return (x_t, y_t)

