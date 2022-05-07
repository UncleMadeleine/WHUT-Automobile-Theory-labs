
from math import *
import matplotlib.pyplot as plt
# 定义常量
m=3880
g=9.8
nmin=600
nmax=4000
L=3.2
a=1.947
hg=0.9
If=0.218
Iw1=1.798
Iw2=3.598
nT=0.85
r=0.367
f=0.013
CDA=2.77
i0=5.83

n=[]
for i in range(nmin,nmax,10):
    n.append(i)
Tq=[]
for i in n:
    Tq.append(-19.313+295.27*(i/1000)-165.44*pow((i/1000),2)+40.874*pow((i/1000),3)-3.8445*pow((i/1000),4))
G=m*g
ig=[5.56,2.769,1.644,1.0,0.793]
Ft1=[]
Ft2=[]
Ft3=[]
Ft4=[]
Ft5=[]
for i in Tq:
    Ft1.append(i*ig[0]*i0*nT/r)
    Ft2.append(i*ig[1]*i0*nT/r)
    Ft3.append(i*ig[2]*i0*nT/r)
    Ft4.append(i*ig[3]*i0*nT/r)
    Ft5.append(i*ig[4]*i0*nT/r)
ua1=[]
ua2=[]
ua3=[]
ua4=[]
ua5=[]
for i in n:
    ua1.append(0.377*r*i/i0/ig[0])
    ua2.append(0.377*r*i/i0/ig[1])
    ua3.append(0.377*r*i/i0/ig[2])
    ua4.append(0.377*r*i/i0/ig[3])
    ua5.append(0.377*r*i/i0/ig[4])
ua=list(range(0,121,5))
# print(ua)
Ff=G*f
Fw=[]
Fz=[]
for i in ua:
    Fw.append(CDA*pow(i,2)/21.15)
    Fz.append(CDA*pow(i,2)/21.15+Ff)
plt.plot(ua1, Ft1, label="Ft1", linewidth=1)
plt.plot(ua2, Ft2, label="Ft2", linewidth=1)
plt.plot(ua3, Ft3, label="Ft3", linewidth=1)
plt.plot(ua4, Ft4, label="Ft4", linewidth=1)
plt.plot(ua5, Ft5, label="Ft5", linewidth=1)
plt.plot(ua5, Ft5, label="Ft5", linewidth=1)
plt.plot(ua, Fz, label="Ff+Fw", linewidth=1)
# TODO:中文字符不能正常输出
plt.title("驱动力-行驶阻力平衡图", fontdict={'size': 20})
plt.xlabel("ua(km/s)", fontdict={'size': 16})
plt.ylabel("Ft(N)", fontdict={'size': 16})

plt.xlim(xmin=0,xmax=120)
plt.legend(loc='upper right')
res=plt.ginput(1)
print("汽车最高车速为%dkm/h"%(res[0][0]))
plt.show()
