from math import *
import matplotlib.pyplot as plt
import matplotlib

# 用于解决中文字体乱码问题
matplotlib.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False




n=[]
for i in range(600,4001,10):
    n.append(i)
Tq=[]
for i in n:
    Tq.append(-19.313+295.27*(i/1000)-165.44*pow(i/1000, 2) +
              40.874*pow(i/1000, 3)-3.8445*pow(i/1000, 4))
m=3880
g=9.8
G=m*g
ig=[5.56,2.769,1.644,1.0,0.793]
nT=0.85
r=0.367
f=0.013
CDA=2.77
i0=5.83
L=3.2
a=1.947
hg=0.9
If=0.218
Iw1=1.798
Iw2=3.598
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
Pe1=[]
Pe2=[]
Pe3=[]
Pe4=[]
Pe5=[]
for i in range(len(n)):
    Pe1.append(Tq[i]*ig[0]*i0*ua1[i]/(3600*r))
    Pe2.append(Tq[i]*ig[1]*i0*ua2[i]/(3600*r))
    Pe3.append(Tq[i]*ig[2]*i0*ua3[i]/(3600*r))
    Pe4.append(Tq[i]*ig[3]*i0*ua4[i]/(3600*r))
    Pe5.append(Tq[i]*ig[4]*i0*ua5[i]/(3600*r))
ua=[]
uamin=0
uamax=119
uastep=0.35
while uamin<=uamax:
    ua.append(uamin)
    uamin=uamin+uastep
Ff=G*f
Fw=[]
for i in ua:
    Fw.append(CDA*pow(i,2)/21.15)
Pf=[]
for i in ua:
    Pf.append(Ff*i/3600)
Pw=[]
for i in range(len(ua)):
    Pw.append(Fw[i]*ua[i]/3600)
Pe0=[]
for i in range(len(ua)):
    Pe0.append(Pf[i]+Pw[i]/nT)
Pe=max(Pe1)
Pe=[Pe]*len(ua)
# print(Pe)

plt.plot(ua1, Pe1, label="1", linewidth=1)
plt.plot(ua2, Pe2, label="2", linewidth=1)
plt.plot(ua3, Pe3, label="3", linewidth=1)
plt.plot(ua4, Pe4, label="4", linewidth=1)
plt.plot(ua5, Pe5, label="5", linewidth=1)
plt.plot(ua, Pe0, label="(Pw+Pf)/et", linewidth=1)
plt.plot(ua, Pe, label="Pe", linewidth=1)
plt.title("汽车功率平衡图")
plt.axis([0,119,0,100])
plt.xlabel("ua(km/h)")
plt.ylabel("Pe(kw)")
plt.legend(loc='upper left')
plt.show()
