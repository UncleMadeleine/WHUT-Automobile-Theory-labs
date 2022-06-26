import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import make_interp_spline
from scipy.interpolate import interp1d
from math import *
import matplotlib

# 用于解决中文字体乱码问题
matplotlib.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False




def speedUpTime(input):
    n1=np.linspace(0,5000)
    nmax=4000
    nmin=600
    global r,yita,CDA,f,G,ig
    i0=0.583
    uamax = [speed(nmax,r,ig[i],i0) for i in range(4)]
    uamin = [speed(nmin,r,ig[i],i0) for i in range(4)]
    ua=[]
    n=[]
    Ttq=[]
    Ft=[]
    F=[]
    delta=[]
    a=[]
    F2=[]
    for i in range(4):
        ua.append(np.linspace(uamin[i],uamax[i],100))
        n.append(round(ua[i],r,ig[i],i0))
        Ttq.append(torque(n[i]))
        Ft.append(force(Ttq[i],ig[i],i0,yita,r))
        F.append(np.array([f*G+CDA*pow(j,2)/21.15 for j in ua[i]]))
        delta.append(1+(1.798+3.598+0.218*pow(i0,2)*pow(ig[i],2)*yita)/(3880*pow(r,2)))
        a.append(1/delta[i]*3880/(Ft[i]-F[i]))
        F2.append(Ft[i]-F[i])
    # print(ua)
    # print(n)
    # print(Ttq)
    # print(Ft)
    # print(F)
    # print(delta)
    # print(a)
    # print(F2)
    temp1=[]
    temp1.append(ua[1]/3.6)
    temp1.append(1/a[1])
    temp2=[[],[]]
    temp3=[[],[]]
    # n1=1
    for j1 in range(100):
        if ua[2][j1] > np.max(ua[1]) and ua[2][j1] <= 70:
            temp2[0].append(ua[2][j1]/3.6)
            temp2[1].append(1/a[2][j1])
    for j1 in range(100):
        if ua[3][j1] > np.max(ua[2]) and ua[3][j1] <= 70:
            temp3[0].append(ua[3][j1]/3.6)
            temp3[1].append(1/a[3][j1])
    # print("长：",len(temp3[0]),len(temp3[1]))
    # y = temp1[0][0]*temp1[1][0]+calculus(np.array(temp1[0]), np.array(temp1[1]))+calculus(np.array(temp2[0]), np.array(
    #     temp2[1]))+calculus(np.array(temp3[0]), np.array(temp3[1]))
    y = temp1[0][0]*temp1[1][0]+calculus(np.array(temp1[0]), np.array(temp1[1]))
    return y


def speed(n,r,ig,i0):
    return 0.377*n*r/ig/i0

def round(ua,r,ig,i0):
    return ig*i0*ua/0.377/r

def torque(nt):
    return np.array([-19.313+295.27*(n/1000)-165.44*pow((n/1000), 2)+40.874*pow((n/1000), 3)-3.8445*pow((n/1000), 4) for n in nt])

def force(Ttq,ig,i0,yita,r):
    return Ttq*ig*i0*yita/r


def calculus(x0,y0):
    n0=np.size(x0)
    n=n0
    # print(np.size(x0))
    x=np.linspace(x0[0],x0[n-1],200)
    # print(x0,y0)
    y=make_interp_spline(x0,y0)(x)
    plt.plot(x,y)
    res=np.trapz(y, x)
    # print(res)
    return res


def fuelExhaustion(i0):
    global G,CDA,yita,m,r,If,Iw1,Iw2,pg,B0,B1,B2,B3,B4,n,ig
    ua4=0.377*n*r/ig[3]/i0
    # print(len(ua4))
    F4=np.array([G*f+CDA*pow(i,2)/21.15 for i in ua4])
    # print(F4)
    P_fw4 = np.array([F4[i]*ua4[i]/(yita*3.6*1000) for i in range(len(ua4))])
    b4=np.array([B0[i]+B1[i]*P_fw4[i]+B2[i]*pow(P_fw4[i],2)+B3[i]*pow(P_fw4[i],3)+B4[i]*pow(P_fw4[i],4) for i in range(len(ua4))])
    # print(b4)
    ua4_m = np.array([25,40,50])
    s_m= np.array([50,250,250])
    # print(len(ua4_m),len(b4))
    b4_m = make_interp_spline(ua4, b4)(ua4_m)
    F4_m = np.array([G*f+CDA*pow(i,2)/21.15 for i in ua4_m])
    P_fw4_m = np.array([F4_m[i]*ua4_m[i]/(yita*3.6*1000) for i in range(len(ua4_m))])
    Q4_m = np.array([P_fw4_m[i]*s_m[i]*b4_m[i]/(1.02*pg*ua4_m[i]) for i in range(len(ua4_m))])
    Q4_a1 = speedUp(40,25,ig[3],0.25,ua4,i0)
    Q4_a2 = speedUp(50,40,ig[3],0.2,ua4,i0)
    Quid=0.299
    tuid=19.3
    s=1075
    Qui=Quid*tuid
    Q4call = (Qui+Q4_a1+Q4_a2+sum(Q4_m))*100/s
    # print(Q4_m,"\n\n",sum(Q4_m))
    return Q4call


def speedUp(umax,umin,ig,a,ua0,i0):
    global f,G, CDA, yita, m, r, If, Iw1, Iw2, pg, B0, B1, B2, B3, B4, n
    ua1=np.array([i for i in range(umin,umax+1)])
    # print(len(ua1))
    delta = 1+(Iw1+Iw2)/(m*pow(r,2))+(If*pow(ig,2)*pow(i0,2)*yita)/(m*pow(r,2))
    P0=np.array([G*f*i/3600+CDA*pow(i,3)/76140+(delta*m*i/3600*a) for i in ua0])
    P=np.array([G*f*i/3600+CDA*pow(i,3)/76140+(delta*m*i/3600*a) for i in ua1])
    dt = 1/(3.6*a)
    b0=np.array([B0[i]+B1[i]*P0[i]+B2[i]*pow(P0[i],2)+B3[i]*pow(P0[i],3)+B4[i]*pow(P0[i],4) for i in range(len(ua0))])
    # print(len(ua0),len(b0))
    b1 = interp1d(ua0, b0, kind='linear')(ua1)
    # print(b1)
    Qt=P*b1/(367.1*pg)
    pw = np.size(Qt)
    # print(pw)
    q=np.sum(Qt)*dt+(Qt[0]+Qt[pw-1])*dt/2
    return q


def main():
    i0=[5.17,5.43,5.83,6.17,6.33]
    y=[]
    b=[]
    for i in i0:
        y.append(speedUpTime(i))
        b.append(fuelExhaustion(i))
    plt.plot(b, y,"+r", label="", linewidth=1)
    b1=np.linspace(b[0],b[4],100)
    y1 = make_interp_spline(b,y)(b1)
    plt.plot(b1,y1,label="?",linewidth=1)
    plt.title("燃油经济性-加速时间曲线")
    plt.xlabel("百公里油耗(L/100km)")
    plt.ylabel("加速时间s")
    plt.show()

m = 3880
g = 9.8
G = m*g
ig = [6.09, 3.09, 1.71, 1.0]
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
pg=7.06
yita=0.85
n=np.array(range(600,4001,1))
# print(n)
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
# print(fuelExhaustion(5))
# print(speedUpTime(5))
main()
