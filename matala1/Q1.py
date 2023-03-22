# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:43:49 2023

@author: berber
"""

##Matala 1 - Q1

def my_func(x1,x2,x3):
    try:
        if (x1+x2+x3)==0:
            return "Not a number – denominator equals zero"
        if type(x1)==int or type(x2)==int or type(x3)==int :
            return "Error: parameters should be float"
        if type(x1)!=float or type(x2)!=float or type(x3)!=float:
            return None
        value=((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
        return value
    except:
            return None


##testing:
print(my_func(1.0, 1.0, 1.0)) #should return value
print(my_func(1, 1.0, 1.0)) #should return Error: parameters should be float
print(my_func('s', 1.0, 1.0)) #should return None
print(my_func(1.0, -1.0, 0)) #should return Not a number – denominator equals zero
        
