'''某海域水深h=3m,有一周期T=15s,波高H=1m的波浪向前传播。
请计算椭圆余弦波的波长并同线性波长作比较
'''

from scipy.integrate import *   #引入积分库（全部）
from sympy import *           #引入sqrt库
from decimal import *       #引入精度函数库(全部)

def K(k):    #定义函数
  return quad(lambda t:1/sqrt((1-(k*sin(t))**2)),0,pi/2)    #lambda定义一个关于t的函数，t不是定值

def E(k):
  return quad(lambda t:sqrt((1-(k*sin(t))**2)),0,pi/2)

def circle_time(T,k,h,H,Ek,Kk):    #定义一个运算周期
  return (4*h*k*Decimal(Kk))/sqrt(3*Decimal(9.8)*H*(1+H/h*(1/k**2 - Decimal(1/2) - 3*Decimal(Ek)/(2*k**2*Decimal(Kk))))),k  #decimal和float不能算术运算
  
def accurate(k=0,t=1):    #定义k初值以及初始精度
  arr = []         #定义空列表
  getcontext().prec = t   #赋予数组精度
  for i in range(1,10):    #从1开始，运算十次
    m = Decimal(i/(10.0**t))+k  
    arr.append(Decimal(m))  #将数放入数组
  return arr

def loop(arr_lst=[],T=15,h=3,H=1):   #定义已知条件，做循环运算
  for i in xrange(len(arr_lst)):    #取数组长度为循环次数     
    Kk,Ke = K(arr_lst[i])
    Ek,Ee = E(arr_lst[i])
    res_1 = list(circle_time(T,arr_lst[i],h,H,Ek,Kk))    #返回结果
    arr_cmp.append(res_1)
  arr_cmp.sort()   
  arr_cmp.reverse()    #结果从大到小排序
  for i in xrange(len(arr_cmp)):
    res,k = arr_cmp[i]
    if res > T:
      continue   #循环
    break        #终止循环
  return res,k,Kk   #返回答案

def B(k,Kk,H,h):
  return sqrt(16*h**3/3/H)*k*Kk

if __name__=='__main__':
  arr_cmp = []   #初始化空数组
  times = 20     #确定精度位数
  k=0           

  try:
    T=int(raw_input('请输入海波周期T = '))
    h=int(raw_input('请输入海面水深h = '))
    H=int(raw_input('请输入海面波高H = '))    
  except:
    T=15
    h=3
    H=1
  print '周期T = ',T ,'s' 
  print '海域水深h = ',h,'m'
  print '波高H = ',H,'m'  
  for j in xrange(times):
    t= j + 1
    arr_lst=accurate(k,t)        
    res,k,Kk=loop(arr_lst,T,h,H)
    L=B(k,Kk,H,h)
    print '第',t,'次计算周期 T = ',res,        
    print '第',t,'次计算 模 k = ',k
    print '波长L=',L
