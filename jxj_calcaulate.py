from numpy import mat
import numpy as np
import math
from sympy import *

pi = math.pi


class Phixrea(object):

    def __init__(self,arr):
        self.arr = arr

    def index(self,id1,id2):
        id1 -= 1
        id2 -= 1
        dst = abs(self.arr[id1]-self.arr[id2]) 
        # print("dst=%s"%dst)
        dmax1 = abs(self.arr[id1]-self.arr[1])
        dmax2 = abs(self.arr[id1]-self.arr[-1])
        if dmax1 >= dmax2:  # 最大的影响范围
            dmax = dmax1
        else:
            dmax = dmax2
        # print("dmax=%s"%dmax)
        r = dst/dmax
        print("R=%s"%r)
        return (1-r)**6*(6+36*r+82*r**2+72*r**3+3*r**4+5*r**5)


def gerator(arr):
    l = len(arr)+1
    p = Phixrea(arr)
    y = np.arange(10,10*l,10).reshape(-1,1)+np.arange(1,l)   # 生成一个二维数组

    for i in np.nditer(y, op_flags=['readwrite']):
        string = str(i)
        phi_x = p.index(int(string[0]),int(string[1]))
        i[...] = phi_x
    return y


class Phix(object):

    def __init__(self,arr):
        self.arr = arr
        # self.x = x


    def index(self,id):
        dst = sqrt((x-self.arr[id])**2)
        dmax1 = abs(self.arr[id]-self.arr[0])
        dmax2 = abs(self.arr[id]-self.arr[-1])
        # return dst/max([dmax1,dmax2])
        r = dst/max([dmax1,dmax2])
        return (1-r)**6*(6+36*r+82*r**2+72*r**3+3*r**4+5*r**5)


def gerator_fc(arr,key):
    # x = Symbol("x")
    p = Phix(arr)
    new_list = [p.index(i) for i in range(len(arr))]
    fc_2 = [diff(i, x) for i in new_list]
    fc_3 = [diff(i,x) for i in fc_2]
    new = []
    fc2 = []
    fc3 = []

    if key == 1:
        for i in range(len(arr)):
            new.append([each.subs(x, arr[i]) for each in new_list])
        return new  # 返回一次导的结果

    if key == 2:
        for i in range(len(arr)):
            fc2.append([each.subs(x, arr[i]) for each in fc_2])
        return fc2  # 返回二次导的结果

    if key == 3:
        for i in range(len(arr)):
            fc3.append([each.subs(x, arr[i]) for each in fc_3])
        return fc3  # 返回三次导的结果


if __name__ == '__main__':
    x = Symbol("x")

    xarr = np.arange(1,30)  # 给出一个一维数组
    A = mat(gerator(xarr)).I  # 得到这个数组的系数矩阵
    print(A)
    # A = gerator(xarr)
    # phi1x = gerator_fc(xarr,1)
    # phi2x = mat(gerator_fc(xarr,2))  # 得到二阶导数值矩阵
    # phi1x = mat(gerator_fc(xarr,1))
    # print(phi1x)