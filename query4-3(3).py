from math import *


# 空载时参数
k = 4080
hgk = 0.845
Lk = 3.95
ak = 2.1
betak = 0.38
bk = Lk-ak

# 满载时参数
mm = 9290
hgm = 1.17
Lm = 3.95
am = 2.95
betam = 0.38
bm = Lm-am

z = []
zmin = 0
zmax = 1
zstep = 0.1
while zmin <= zmax:
    z.append(zmin)
    zmin = zmin+zstep

fai = z
fai_fk = []
fai_fm = []
fai_rk = []
fai_rm = []
for i in z:
    fai_fk.append(betak*i*Lk/(bk+i*hgk))
    fai_fm.append(betam*i*Lm/(bm+i*hgm))
    fai_rk.append((1-betak)*i*Lk/(ak-i*hgk))
    fai_rm.append((1-betam)*i*Lm/(am-i*hgm))
Efk = []
Efm = []
Erk = []
Erm = []
for i in range(1, len(z)):
    # print(fai_fk[i])
    Efk.append(z[i]/fai_fk[i]*100)
    Efm.append(z[i]/fai_fm[i]*100)
    Erk.append(z[i]/fai_rk[i]*100)
    Erm.append(z[i]/fai_rm[i]*100)
t1 = 0.02
t2 = 0.02
ua0 = 30
fai = 0.8
g = 9.8
# print(len(Erk))
ak1 = ak*g*fai/(Lk+fai*hgk)
am1 = am*g*fai/(Lm+fai*hgm)
ak2= bk*g*fai/(Lk-fai*hgk)
am2 = bm*g*fai/(Lm-fai*hgm)
Sk1 = (t1+t2/2)*ua0/3.6+pow(ua0, 2)/(25.92*ak1)
Sk2 = (t1+t2/2)*ua0/3.6+pow(ua0, 2)/(25.92*am1)
Sk3 = (t1+t2/2)*ua0/3.6+pow(ua0, 2)/(25.92*ak2)
Sk4 = (t1+t2/2)*ua0/3.6+pow(ua0, 2)/(25.92*am2)
print("在前制动器损坏时：空载时，汽车制动距离为%.3lfm；满载时，汽车制动距离为%.3lfm" % (Sk1, Sk2))
print("在后制动器损坏时：空载时，汽车制动距离为%.3lfm；满载时，汽车制动距离为%.3lfm" % (Sk3, Sk4))
