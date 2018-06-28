'''ĳ����ˮ��h=3m,��һ����T=15s,����H=1m�Ĳ�����ǰ������
�������Բ���Ҳ��Ĳ�����ͬ���Բ������Ƚ�
'''

from scipy.integrate import *   #������ֿ⣨ȫ����
from sympy import *           #����sqrt��
from decimal import *       #���뾫�Ⱥ�����(ȫ��)

def K(k):    #���庯��
  return quad(lambda t:1/sqrt((1-(k*sin(t))**2)),0,pi/2)    #lambda����һ������t�ĺ�����t���Ƕ�ֵ

def E(k):
  return quad(lambda t:sqrt((1-(k*sin(t))**2)),0,pi/2)

def circle_time(T,k,h,H,Ek,Kk):    #����һ����������
  return (4*h*k*Decimal(Kk))/sqrt(3*Decimal(9.8)*H*(1+H/h*(1/k**2 - Decimal(1/2) - 3*Decimal(Ek)/(2*k**2*Decimal(Kk))))),k  #decimal��float������������
  
def accurate(k=0,t=1):    #����k��ֵ�Լ���ʼ����
  arr = []         #������б�
  getcontext().prec = t   #�������龫��
  for i in range(1,10):    #��1��ʼ������ʮ��
    m = Decimal(i/(10.0**t))+k  
    arr.append(Decimal(m))  #������������
  return arr

def loop(arr_lst=[],T=15,h=3,H=1):   #������֪��������ѭ������
  for i in xrange(len(arr_lst)):    #ȡ���鳤��Ϊѭ������     
    Kk,Ke = K(arr_lst[i])
    Ek,Ee = E(arr_lst[i])
    res_1 = list(circle_time(T,arr_lst[i],h,H,Ek,Kk))    #���ؽ��
    arr_cmp.append(res_1)
  arr_cmp.sort()   
  arr_cmp.reverse()    #����Ӵ�С����
  for i in xrange(len(arr_cmp)):
    res,k = arr_cmp[i]
    if res > T:
      continue   #ѭ��
    break        #��ֹѭ��
  return res,k,Kk   #���ش�

def B(k,Kk,H,h):
  return sqrt(16*h**3/3/H)*k*Kk

if __name__=='__main__':
  arr_cmp = []   #��ʼ��������
  times = 20     #ȷ������λ��
  k=0           

  try:
    T=int(raw_input('�����뺣������T = '))
    h=int(raw_input('�����뺣��ˮ��h = '))
    H=int(raw_input('�����뺣�沨��H = '))    
  except:
    T=15
    h=3
    H=1
  print '����T = ',T ,'s' 
  print '����ˮ��h = ',h,'m'
  print '����H = ',H,'m'  
  for j in xrange(times):
    t= j + 1
    arr_lst=accurate(k,t)        
    res,k,Kk=loop(arr_lst,T,h,H)
    L=B(k,Kk,H,h)
    print '��',t,'�μ������� T = ',res,        
    print '��',t,'�μ��� ģ k = ',k
    print '����L=',L
