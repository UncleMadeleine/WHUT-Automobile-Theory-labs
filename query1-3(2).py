from math import *
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
ua1 = []
for i in n:
    ua1.append(0.377*r*i/i0/ig[0])
Ff=G*f
Fw = []
Fz = []
for i in ua1:
    Fw.append(CDA*pow(i, 2)/21.15)
    Fz.append(CDA*pow(i, 2)/21.15+Ff)
Fi1=[]
for i in range(len(n)):
    Fi1.append(Ft1[i]-Fz[i])
maxF=0
for i in Fi1:
    if i >maxF:
        maxF=i
imax=100*tan(asin(maxF/G))
print("汽车最大爬坡度为%f%%"%imax)