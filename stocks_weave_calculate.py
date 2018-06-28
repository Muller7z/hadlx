
from scipy.optimize import fsolve
from pylab import*


def hyper_eqiton(x):
    """用来返回fcuntion的对象：即超越方程"""
    # 定义参数:lamda & Lenth
    lamda = float(x[0])
    Lenth = float(x[1])
    c = math.cosh((2*math.pi/Lenth)*h)
    s = math.sinh((2*math.pi/Lenth)*h)
    B33 = (318*c**6 + 1/(64*s**6))
    B35 = (88128*c**14-208224*c**12+70848*c**10+54000*c**8-21816 *
           c**6+6264*c**4-54*c**2-81)/(12288*s**12*(6*c**2-1))
    B55 = (19200*c**16-262720*c**14+83680*c**12+20160*c**10-7280*c**8+7160*c **
           6-1800*c**4-1050*c**2+225)/(12288*s**10*(6*c**2-1)*(8*c**4-11*c**2+3))
    C1 = (8*c**4-8*c**2+9)/(8*s**4)
    C2 = (3840*c**12-4096*c**10+2592*c**8-1008*c**6 +
          5944*c**4-1830*c**2+147)/(512*s**10*(6*c**2-1))

    return [
        lamda*Lenth*(1+lamda*lamda*B33+lamda**4*(B35+B55))-math.pi*H,
        (9.8*T*T*math.tanh(2*math.pi/Lenth)*h) *
        (1+lamda*lamda*C1+lamda**4*C2)-Lenth
    ]


def fc_eta(lamda, Lenth, h):
    """这个函数是用来绘制 eta 函数的图像的"""
    # t轴的取值，从0到4pi，取了1000个值
    t = np.linspace(0, 4*np.pi, num=1000)
    # 生成eta：一个数组，都是对应于t的eta值
    eta = [Eta(i, lamda, Lenth, h) for i in t]
    plt.plot(t, eta[:], label='eta')
    xlabel('time')
    ylabel('eta')
    # 三个命令生成图像
    plt.legend()
    plt.grid()
    plt.show()


def Eta(t, l, L, h):
    """这个函数：输入一个t 输出对应的eta值"""
    k = 2*math.pi/L
    c = math.cosh(k*h)
    s = math.sinh(k*h)
    B22 = (2*c**2+1)*c/(4*s**3)
    B24 = (272*c**8-504*c**6-192*c**4+332*c**2+24)*c/(384*s**9)
    B44 = (768*c**10-488*c**8-48*c**6+48*c**4 +
           106*c**2-21)*c/(384*s**9*(6*c**2-1))
    B33 = (318*c**6 + 1/(64*s**6))
    B35 = (88128*c**14-208224*c**12+70848*c**10+54000*c**8-21816 *
           c**6+6264*c**4-54*c**2-81)/(12288*s**12*(6*c**2-1))
    B55 = (19200*c**16-262720*c**14+83680*c**12+20160*c**10-7280*c**8+7160*c **
           6-1800*c**4-1050*c**2+225)/(12288*s**10*(6*c**2-1)*(8*c**4-11*c**2+3))
    # 这几个值是自己取的
    x = np.pi / 2
    omega = 1
    lamda = [l, l**2*B22+l**4*B24, l**3*B33 + l**5 *
             B35, l**3*B33 + l**5*B35, l**4*B44, l*5*B55]
    # 通过求和函数，解出n从1到5的，与t对应的eta值
    return math.fsum([lamda[n-1]*math.cos(n*(k*x-omega*t)) for n in range(1, 6)])/k


if __name__ == '__main__':
    while True:
        T = float(input("请输入周期（s）："))
        h = float(input("请输入水深（m）："))
        H = float(input("请输入波高（m)："))
        # 调用fslove函数解超越方程，求解完成后返回一个列表（result）
        result = fsolve(hyper_eqiton, np.array([0.001, 125.457]))
        lamda = result[0]
        L = result[1]
        C = L/float(T)
        print('lamda={:.5},L={:.5}'.format(lamda, L))
        print("波速={:.5}".format(C))
        fc_eta(lamda, L, h)

        go = input('输入回车继续运行,输入 n 回车结束运行: ')
        if go == 'n':
            break
