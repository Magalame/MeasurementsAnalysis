import numpy as np
#def durbinWatson():

def weighted_mean(x,err_x,axis=1):
    x = np.array(x)
    err_x = np.array(err_x)
    
    w = 1/err_x**2
    
    sum_w = np.sum(w,axis=axis)
    
    mean_x = np.sum(np.multiply(x,w),axis=axis)/sum_w
    
    err_mean = sum_w**(-0.5)
    
    return mean_x, err_mean