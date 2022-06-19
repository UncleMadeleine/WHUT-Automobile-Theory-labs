from math import *
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# 用于解决中文字体乱码问题
matplotlib.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False


# 定义常量
m = 3880
g = 9.8
nmin = 600
nmax = 4000
L = 3.2
a = 1.947
hg = 0.9
If = 0.218
Iw1 = 1.798
Iw2 = 3.598
nT = 0.85
r = 0.367
f = 0.013
CDA = 2.77
i0 = 5.83

n = []
for i in range(nmin, nmax, 10):
    n.append(i)
Tq = []
for i in n:
    Tq.append(-19.313+295.27*(i/1000)-165.44*pow((i/1000), 2) +
              40.874*pow((i/1000), 3)-3.8445*pow((i/1000), 4))
G = m*g
ig = [5.56, 2.769, 1.644, 1.0, 0.793]
Ft1 = []
Ft2 = []
Ft3 = []
Ft4 = []
Ft5 = []
for i in Tq:
    Ft1.append(i*ig[0]*i0*nT/r)
    Ft2.append(i*ig[1]*i0*nT/r)
    Ft3.append(i*ig[2]*i0*nT/r)
    Ft4.append(i*ig[3]*i0*nT/r)
    Ft5.append(i*ig[4]*i0*nT/r)
ua1 = []
ua2 = []
ua3 = []
ua4 = []
ua5 = []
for i in n:
    ua1.append(0.377*r*i/i0/ig[0])
    ua2.append(0.377*r*i/i0/ig[1])
    ua3.append(0.377*r*i/i0/ig[2])
    ua4.append(0.377*r*i/i0/ig[3])
    ua5.append(0.377*r*i/i0/ig[4])
Fw1 = []
Fw2 = []
Fw3 = []
Fw4 = []
Fw5 = []
for i in range(len(ua1)):
    Fw1.append(CDA*pow(ua1[i], 2)/21.15)
    Fw2.append(CDA*pow(ua2[i], 2)/21.15)
    Fw3.append(CDA*pow(ua3[i], 2)/21.15)
    Fw4.append(CDA*pow(ua4[i], 2)/21.15)
    Fw5.append(CDA*pow(ua5[i], 2)/21.15)
Ff=G*f
deta1 = 1+(Iw1+Iw2)/(m*pow(r,2))+(If*pow(ig[0],2)*pow(i0,2)*nT)/(m*pow(r,2))
deta2 = 1+(Iw1+Iw2)/(m*pow(r,2))+(If*pow(ig[1],2)*pow(i0,2)*nT)/(m*pow(r,2))
deta3 = 1+(Iw1+Iw2)/(m*pow(r,2))+(If*pow(ig[2],2)*pow(i0,2)*nT)/(m*pow(r,2))
deta4 = 1+(Iw1+Iw2)/(m*pow(r,2))+(If*pow(ig[3],2)*pow(i0,2)*nT)/(m*pow(r,2))
deta5 = 1+(Iw1+Iw2)/(m*pow(r,2))+(If*pow(ig[4],2)*pow(i0,2)*nT)/(m*pow(r,2))
a1=[]
a2=[]
a3=[]
a4=[]
a5=[]
for i in range(len(n)):
    a1.append((Ft1[i]-Ff-Fw1[i])/(deta1*m))
    a2.append((Ft2[i]-Ff-Fw2[i])/(deta2*m))
    a3.append((Ft3[i]-Ff-Fw3[i])/(deta3*m))
    a4.append((Ft4[i]-Ff-Fw4[i])/(deta4*m))
    a5.append((Ft5[i]-Ff-Fw5[i])/(deta5*m))
ad1=[]
ad2=[]
ad3=[]
ad4=[]
ad5=[]
for i in range(len(n)):
    ad1.append(1/a1[i])
    ad2.append(1/a2[i])
    ad3.append(1/a3[i])
    ad4.append(1/a4[i])
    ad5.append(1/a5[i])
plt.plot(ua1,ad1,label="1/a1")
plt.plot(ua2,ad2,label="1/a2")
plt.plot(ua3,ad3,label="1/a3")
plt.plot(ua4,ad4,label="1/a4")
plt.plot(ua5,ad5,label="1/a5")
plt.axis([0,99,0,10])
plt.title("汽车的加速度倒数取线", fontdict={'size': 20})
plt.xlabel("ua(km/s)", fontdict={'size': 16})
plt.ylabel("1/a", fontdict={'size': 16})
plt.legend(loc='upper right')
a=max(np.array(a1))
af = asin(max(np.array(Ft1)-Ff-np.array(Fw1))/G)
C= tan(af)/(a/L+hg*tan(af)/L)
print("假设后轮驱动，最大爬坡度相应的附着率为%.4lf" % (C))
plt.show()
