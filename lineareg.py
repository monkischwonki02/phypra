from sklearn.linear_model import LinearRegression
import numpy as np

'''
# transforms 1D-Coordinates with a defined transformation
# parameters:
# x - np.ndarray (n,): coordinates to be transformed
# transform - function (lambda) : function to transform coordinated 
#
# return transformed coordinates
'''
def transform_Coord(x,transform):
    return transform(x)

'''
# transforms 2D-Coordinates with a defined transformation
# parameters:
# x - np.ndarray (n,): coordinates to be transformed
# y - np.ndarray (n,): coordinates to be transformed
# transform - function (lambda) : function to transform coordinated 
#
# return:
# tupel with the transformed coordinates (x_t, y_t)
# x_t - np.ndarray (n,) : transformed coordinates
# y_t - np.ndarray (n,) : transformed coordinates
'''
def transform_Coord(x,y,transform):
    x_t = transform(x)
    y_t = transform(y)
    return (x_t, y_t)

'''
# creates a Linear Regression Model based on x,y of the data
# 
# parameters:
# x - np.ndarray (n,) : x-coordinates of the data
# y - np.ndarray (n,) : y-coordinates of the data
#
# return
# tupel with the slope (a) and the intercept (b) of the regression-line (y = a*x + b)
'''
def create_Lin_Model(x,y):
    model = LinearRegression()
    model.fit(x.reshape(-1,1), y.reshape(-1,1))
    return (model.coef_.reshape(-1)[0], model.intercept_[0])

'''
# calculate the std of y, the slope (a) and the intercept (b) of the regression line
#
# parameters:
# x,y - np.ndarray (n,) : x,y of data (same as the data to train the regression-model)
# a - float : slope of regression line
# b - float : intercept of regression line
#
# return:
# tupel with std of y, a and b
'''
def calc_std(x,y,a,b):
    s_y = np.sqrt(1/(len(x) - 2) * np.sum((y - (a*x + b))**2))
    s_a = s_y * np.sqrt(len(x) / (len(x) * np.sum(x**2) - np.sum(x)**2))
    s_b = s_y * np.sqrt(np.sum(x**2) / (len(x) * np.sum(x**2) - np.sum(x)**2))

    return (s_y, s_a, s_b)
