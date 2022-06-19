from math import *
import matplotlib.pyplot as plt
import matplotlib

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


G = m*g
ig = [5.56, 2.769, 1.644, 1.0, 0.793]
u1=[]
u2=[]
for i in ig:
    u1.append(0.377*r*nmin/i0/i)
    u2.append(0.377*r*nmax/i0/i)
deta=[]
for i in ig:
    deta.append(1+(Iw1+Iw2)/(m*pow(r,2))+(If*pow(i,2)*pow(i0,2)*nT)/(m*pow(r,2)))
ua=[]
uas=6.0
uae=99.0
while uas<=uae:
    ua.append(uas)
    uas+=0.01
N=len(ua)
n=0
Tq=0
Ft=0
inv_a=len(ua)*[0]
delta=len(ua)*[0]
Ff=G*f
Fw=[]
for i in ua:
    Fw.append(CDA*pow(i,2)/21.15)
t=[]
for i in range(N):
    k=i
    ans=0
    if ua[i]<=u2[1]:
        n=ua[i]*(ig[1]*i0/r)/0.377
        Tq=-19.313+295.27*(n/1000)-165.44*pow((n/1000), 2) + 40.874*pow((n/1000), 3)-3.8445*pow((n/1000), 4)
        Ft=Tq*ig[1]*i0*nT/r
        inv_a[i]=(deta[1]*m)/(Ft-Ff-Fw[i])
        delta[i]=0.01*inv_a[i]/3.6
    elif ua[i]<=u2[2]:
        n=ua[i]*(ig[2]*i0/r)/0.377
        Tq=-19.313+295.27*(n/1000)-165.44*pow((n/1000), 2) + 40.874*pow((n/1000), 3)-3.8445*pow((n/1000), 4)
        Ft=Tq*ig[2]*i0*nT/r
        inv_a[i]=(deta[2]*m)/(Ft-Ff-Fw[i])
        delta[i]=0.01*inv_a[i]/3.6
    elif ua[i]<=u2[3]:
        n=ua[i]*(ig[3]*i0/r)/0.377
        Tq=-19.313+295.27*(n/1000)-165.44*pow((n/1000), 2) + 40.874*pow((n/1000), 3)-3.8445*pow((n/1000), 4)
        Ft=Tq*ig[3]*i0*nT/r
        inv_a[i]=(deta[3]*m)/(Ft-Ff-Fw[i])
        delta[i]=0.01*inv_a[i]/3.6
    else:
        n=ua[i]*(ig[4]*i0/r)/0.377
        Tq=-19.313+295.27*(n/1000)-165.44*pow((n/1000), 2) + 40.874*pow((n/1000), 3)-3.8445*pow((n/1000), 4)
        Ft=Tq*ig[4]*i0*nT/r
        inv_a[i]=(deta[4]*m)/(Ft-Ff-Fw[i])
        delta[i]=0.01*inv_a[i]/3.6
    for j in range(k):
        ans+=delta[j]
    t.append(ans)
plt.plot(t, ua)
plt.title("汽车二档原地换挡起步加速时间曲线", fontdict={'size': 20})
plt.xlabel("时间t(s)", fontdict={'size': 16})
plt.ylabel("速度ua(km/h)", fontdict={'size': 16})

plt.xlim(xmin=0, xmax=80)
plt.ylim(ymin=0, ymax=100)
# plt.legend(loc='upper right')
res = plt.ginput(1)
print("汽车二档原地换挡起步加速至%.3lfkm/h所需的时间为%.3lfs" % (res[0][1],res[0][0]))
plt.show()
