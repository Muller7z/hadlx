import numpy as np
from numpy import mat
from sympy import *
import pylab as plt
from radial_main import RadialHandle

# 定义一个符号变量“x” 求导需要
x = Symbol("x")
# 初始化一个x向量
xarr = np.arange(1,4,dtype='float')
# 实例化一个对象
radial = RadialHandle(xarr)
# 调用实例的deriva方法，并传入一个参数1，返回一阶导的系数矩阵
Phix = radial.deriva(1)
# print(Phix)
print("phi1x###################################")
# 调用实例的一个方法，返回0阶导的系数矩阵，没有将这个方法合并到上一个的原因是
# 求得的系数矩阵不能求逆，奇异矩阵报错，产生原因不明
invA = mat(radial.calcaulate_A()).I
# print(invA)
print("inva####################################")
# 这是和微分方程有关的一个系数，利用diag方法将其转换为对角矩阵
C = mat(diag(radial.constans_handle()))
# print(C)
print("c#######################################")
# 矩阵组合，得到一个全系数矩阵
FullC = Phix * invA + C
# print(FullC)
print("fullc###################################")


def changeto01(arr):
    """这个函数就是传说中的化01矩阵了，为了带入初值条件"""
    harr = arr[:,0]
    newh = [-1.3373*each for each in harr]
    newh[0] = 1
    arr[0,:] = [0 for i in range(len(arr))]
    arr[:,0] = [0 for i in range(len(arr))]
    arr[0,0] = 1
    arr01 = arr
    # 返回一个tuple
    return arr01,newh


if __name__ == '__main__':
    # 调用上一个函数，带入初值条件
    # dtype="float" 否则报错：No loop matching the specified signature and casting
    r = changeto01(np.array(FullC,dtype='float'))
    constant = r[0]
    yyy = r[1]
    print(constant)
    print("01mat###################################")
    print(yyy)
    print("coffy###################################")

    try:
        # 解方程组，得到H是一个列向量
        H = np.linalg.solve(constant,yyy)
        print(H)
        print("H####################################")
        # 画图
        plt.plot(xarr, H, label='H')
        plt.legend()
        plt.grid()
        plt.show()
    except TypeError as ep:
        print(ep)
