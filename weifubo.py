

import math


def lk(l,T,h):
    k = 2*math.pi / l
    return (9.8*T*T*math.tanh(k*h))/(2*math.pi) 


def cycle(T,h):

    def lk(l,T,h):
        k = 2*math.pi / l
        return (9.8*T*T*math.tanh(k*h))/(2*math.pi) 

    l = 50  # 取个波长的初始值，然后开始暴力计算
    while True:
        L = lk(l,T,h)
        print(L)
        if abs(L-l) <= 0.01:
            return L
        else:
            if L - l > 0:
                l+=0.01  # 步进值
            elif L - l < 0:
                l -= 0.01
            else:
                return L


def format_output(float_num):
    string = str(float(float_num))
    dot = string.index(".")
    return string[:dot+4]  # 保留至小数点后三位


if __name__ == '__main__':
    while True:
        T = float(input("请输入周期（s）："))
        h = float(input("请输入水深（m）："))
        L = cycle(T,h)
        C = L/T
        print("迭代后得到波长L=%s m（精度保持到小数点后2位）"%format_output(L))
        print("波速v=%s m/s"%format_output(C))
        go = input('输入回车继续运行,输入 n 回车结束运行: ')
        if go == 'n':
            break
