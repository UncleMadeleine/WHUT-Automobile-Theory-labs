from math import *
import matplotlib.pyplot as plt


# 空载时参数
k=4080
hgk=0.845
Lk=3.95
ak=2.1
betak=0.38
bk=Lk-ak

# 满载时参数
mm=9290
hgm=1.17
Lm=3.95
am=2.95
betam=0.38
bm=Lm-am

z=[]
zmin = 0
zmax = 1
zstep = 0.1
while zmin <= zmax:
    z.append(zmin)
    zmin = zmin+zstep
plt.figure(1)
fai=z
fai_fk=[]
fai_fm=[]
fai_rk=[]
fai_rm=[]
for i in z:
    fai_fk.append(betak*i*Lk/(bk+i*hgk))
    fai_fm.append(betam*i*Lm/(bm+i*hgm))
    fai_rk.append((1-betak)*i*Lk/(ak-i*hgk))
    fai_rm.append((1-betam)*i*Lm/(am-i*hgm))
plt.plot(fai,z,label="z",linewidth=1)
plt.plot(fai,fai_fk,label="front-empty",linewidth=1)
plt.plot(fai,fai_fm,label="front-full",linewidth=1)
plt.plot(fai,fai_rk,label="rear-empty",linewidth=1)
plt.plot(fai,fai_rm,label="rear-full",linewidth=1)
# TODO:中文字符不能正常输出
plt.title("利用附着系数与制动强度关系曲线")
plt.xlabel("(z/g)")
plt.ylabel("利用附着系数")
plt.legend(loc='upper left')
# plt.show()





plt.figure(2)
Efk=[]
Efm=[]
Erk=[]
Erm=[]
for i in range(1,len(z)):
    # print(fai_fk[i])
    Efk.append(z[i]/fai_fk[i]*100)
    Efm.append(z[i]/fai_fm[i]*100)
    Erk.append(z[i]/fai_rk[i]*100)
    Erm.append(z[i]/fai_rm[i]*100)
plt.plot(fai_fk[1:],Efk,label="front-empty",linewidth=1)
plt.plot(fai_fm[1:],Efm,label="front-full",linewidth=1)
plt.plot(fai_rk[1:],Erk,label="rear-empty",linewidth=1)
plt.plot(fai_rm[1:],Erm,label="rear-full",linewidth=1)
# TODO:中文问题
plt.title("前后制动效率曲线")
plt.xlabel("附着系数")
plt.ylabel("制动效率")
plt.axis([0, 1, 0, 100])
plt.legend(loc='lower left')
plt.show()
