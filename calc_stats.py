import scipy.stats as scs
import numpy as np

''' 
# returns the tau for the students-t-distribution for an given convidence interval
# and a given degree of freedom
# note: the convidence interval is mutual
#
# args:
# ci - float : convidence interval
# df - int : degrees of freedom
'''
def return_T(ci, df):
    return scs.t.ppf((1+ci)/2, df)

'''
# returns the mean, standard deviation, std of mean of the data
# for the std we use degrees of freedom: n-1 (ddof=1)
#
# args:
# data - np.ndarray : shape (n,)
#
# return:
# mean, std and std_mean in a tupel
'''
def calc_Stat(data):
    mean = np.mean(data)
    std = np.std(data, ddof=1) 
    std_mean = std/np.sqrt(len(data))
    
    return (mean, std, std_mean)

'''
# returns random- and systematitical inaccuracy 
#
# args:
# a, b - float: variable for systematical inaccuracy (a + b*x)
# data - np.ndarray : shape (n,)
#
# return:
# d_s, d_z, d_s + d_z as tupel
# d_s - float : systematical inaccuracy
# d_z - float : random inaccuracy
'''
def calc_InAcc(a, b, data):
    (mean, std, std_mean) = calc_Stat(data)
    d_s = a + b*mean
    d_z = return_T(0.95, len(data)-1)*std_mean
    
    return (d_s, d_z, d_s+d_z)
    
    


