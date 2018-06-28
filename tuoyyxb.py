# Python 3 

from scipy.integrate import *  # 引入积分库（全部）
from sympy import *  # 引入sqrt库
from decimal import *  # 引入精度函数库(全部)
import math  


def KK(theta,k):  
    return 1/(sqrt(1-(k*sin(theta))**2))


def EE(theta,k):
    return sqrt(1-(k*sin(theta))**2)


def Kk(k):
    return quad(KK,0,math.pi/2,args=(k))[0]


def Ek(k):
    return quad(EE,0,math.pi/2,args=(k))[0]


def handleT(k):
    # return (4*h*k*Kk(k))/math.sqrt((3*9.8*H)*(1+(H/h)*(2/k**2 -1 -(3*Ek(k))/(k**2*Kk(k)))))
    return 15*k*k



def divide2(left,right):
    # count = 1

    left_T,right_T = handleT(left),handleT(right)
    if abs(T-left_T) < abs(T - right_T):
    # 左边更接近
        print(left,right+right/2,left_T,"left")
        return left,right+right/2,left_T,"left"


    else:
    # 右边更接近
        print(left+left/2,right,right_T,"right")
        return left+left/2,right,right_T,"right"


if __name__ == "__main__":

    T = 15
    h = 3
    H = 1
    DECIMAL = 0.0000001
    left = 0.7
    right = 0.9
    while abs(divide2(left,right)[2] - T) >= 0.001:
        left,right = divide2(left,right)[0],divide2(left,right)[1]



    

