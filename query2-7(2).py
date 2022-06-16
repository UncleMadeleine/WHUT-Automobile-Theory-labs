
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import make_interp_spline
n=[]
for i in range(600,4001,1):
    n.append(i)
m = 3880
g = 9.8
G = m*g
ig = [5.56, 2.769, 1.644, 1.0, 0.793]
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
n0=np.array([815,1207,1614,2012,2603,3006,3403,3804])
VB0 = np.array([1326.8,1354.7,1284.4,1122.9,1141.0,1051.2,1233.9,1129.7])
VB1 = np.array([-416.46,-303.98,-189.75,-121.59,-98.893,-73.714,-84.478,-45.291])
VB2 = np.array([72.379,36.657,14.524,7.0035,4.4763,2.8593,2.9788,0.71113])
VB3 = np.array([-5.8629,-2.0553,-0.51184,-0.18517,-0.091077,-0.05138,-0.047449,-0.00075215])
VB4 = np.array([0.17768,0.043072,0.0068164,0.0018555,0.00068906,0.00035032,0.00028230,-0.000038568])
B0 = make_interp_spline(n0, VB0)(n)
B1 = make_interp_spline(n0, VB1)(n)
B2 = make_interp_spline(n0, VB2)(n)
B3 = make_interp_spline(n0, VB3)(n)
B4 = make_interp_spline(n0, VB4)(n)
# print(len(B0))
Ff=G*f
ua4=[]
ua5=[]
Fz4=[]
Fz5=[]
Pe4=[]
Pe5=[]
for i in range(len(n)):
    ua4.append(0.377*r*n[i]/i0/ig[3])
    ua5.append(0.377*r*n[i]/i0/ig[4])
    Fz4.append(Ff+CDA*pow(ua4[i],2)/21.15)
    Fz5.append(Ff+CDA*pow(ua5[i],2)/21.15)
    Pe4.append(Fz4[i]*ua4[i]/(nT*3.6*1000))
    Pe5.append(Fz5[i]*ua5[i]/(nT*3.6*1000))
b4=[]
b5=[]
for i in range(len(n)):
    b4.append(B0[i]+B1[i]*pow(Pe4[i],1)+B2[i]*pow(Pe4[i],2)+B3[i]*pow(Pe4[i],3)+B4[i]*pow(Pe4[i],4))
    b5.append(B0[i]+B1[i]*pow(Pe5[i],1)+B2[i]*pow(Pe5[i],2)+B3[i]*pow(Pe5[i],3)+B4[i]*pow(Pe5[i],4))
pg=7
Q4=[]
Q5=[]
for i in range(len(n)):
    Q4.append(b4[i]*Pe4[i]/(1.02*pg*ua4[i]))
    Q5.append(b5[i]*Pe5[i]/(1.02*pg*ua5[i]))
plt.plot(ua4, Q4, label="4", linewidth=1)
plt.plot(ua5, Q5, label="5", linewidth=1)
# TODO:中文问题
plt.title("最高档与次高档等速百公里油耗曲线")
plt.xlabel("ua(km/h)")
plt.ylabel("百公里油耗(L/100km)")
plt.axis([0, 100, 10, 30])
plt.legend(loc='upper left')
plt.show()
