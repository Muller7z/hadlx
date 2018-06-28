
import numpy as np
from numpy import mat
from sympy import *

x = Symbol("x")


class RadialHandle(object):
    """这个类绑定了几个函数，用来计算径向基函数相关的矩阵"""
    def __init__(self,arr):
        self.arr = arr

    def index_r(self, p, x):
        """计算系数矩阵相关"""
        dst = abs(self.arr[p] - self.arr[x])
        dmax1 = abs(self.arr[p] - self.arr[0])
        dmax2 = abs(self.arr[p] - self.arr[-1])
        dmax = max([dmax1, dmax2])
        r = dst / dmax
        return (1 - r) ** 6 * (6 + 36 * r + 82 * r ** 2 + 72 * r ** 3 + 3 * r ** 4 + 5 * r ** 5)

    def calcaulate_A(self):
        """计算系数矩阵的主函数，直接返回系数矩阵"""
        new = []
        for i in range(len(self.arr)):
            new.append([self.index_r(phi, i) for phi in range(len(self.arr))])
        return mat(np.array(new))

    def index(self,pp,xx,key):
        """为实现求导的前置方法，此处使用的求导方法先判断元素的位置，再求导，避免了nan值出现
           较消r的方法更通用，更容易理解。我写过一个传统的消r法，验证1阶导计算结果二者完全一致
        """
        dst1 = x - self.arr[pp]
        dst2 = self.arr[pp] - x
        dmax1 = abs(self.arr[pp]-self.arr[0])
        dmax2 = abs(self.arr[pp]-self.arr[-1])
        dmax = max([dmax1,dmax2])
        if pp <= xx:
            r = dst1/dmax
            r_x1 = diff((1-r)**6*(6+36*r+82*r**2+72*r**3+3*r**4+5*r**5),x)
            r_x2 = diff(r_x1,x)
            if key == 1:
                return r_x1
            if key == 2:
                return r_x2
        if pp > xx:
            r = dst2/dmax
            r_x1 = diff((1-r)**6*(6+36*r+82*r**2+72*r**3+3*r**4+5*r**5),x)
            r_x2 = diff(r_x1,x)
            if key == 1:
                return r_x1
            if key == 2:
                return r_x2

    def deriva(self,key):
        """此方法为求导的主方法，key代表1阶、2阶导，目前只实现了2阶及以下的"""
        if key == 1:
            phi_1x = []
            for xx in range(len(self.arr)):
                phi_1x.append([self.index(pp,xx,key).subs(x,self.arr[xx]) for pp in range(len(self.arr))])
            return phi_1x

        if key == 2:
            phi_2x = []
            for xx in range(len(self.arr)):
                phi_2x.append([self.index(pp,xx,key).subs(x,self.arr[xx]) for pp in range(len(self.arr))])
            return phi_2x

    def handle_x(self,x):
        """下一个函数的前置函数"""
        return ((9.4365*10**-5)/(1.9485-0.05*x)**1.5) + (0.0125/(1.9845-0.05*x))

    def constans_handle(self):
        """计算常数矩阵，因计算方程的不同，这个函数就需要更改"""
        return [self.handle_x(xx) for xx in self.arr]


if __name__ == '__main__':

    pass
