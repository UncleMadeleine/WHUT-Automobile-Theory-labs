from math import *
n=[]
for i in range(6000,4001,10):
    n.append(i)
Tq=[]
for i in n:
    Tq.append(-19.313+295.27*(n/1000)-165.44*pow(n/1000,2)+40.874*(n/1000,3)-3.8445*pow(n/1000,4))
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
