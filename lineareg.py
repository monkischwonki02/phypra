from sklearn.linear_model import LinearRegression
import numpy as np

'''
# creates a Linear Regression Model based on x,y of the data
# 
# args:
# x - np.ndarray (n,) : x-coordinates of the data
# y - np.ndarray (n,) : y-coordinates of the data
#
# return
# tupel with the slope (a) and the intercept (b) of the regression-line (y = a*x + b)
'''
def create_lin_model(x,y):
    model = LinearRegression()
    model.fit(x.reshape(-1,1), y.reshape(-1,1))
    return (model.coef_.reshape(-1)[0], model.intercept_[0])

'''
# calculate the std of y, the slope (a) and the intercept (b) of the regression line
#
# args:
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
