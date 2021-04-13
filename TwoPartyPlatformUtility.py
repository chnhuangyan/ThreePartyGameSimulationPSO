import Data as data
import numpy as np
import matplotlib.pyplot as plt
import math

q = data.q
g = [0,1,2,3]
c = data.C
b = data.b
n = 3
P = data.P

Up1=[0,0,0,0]
Up2=[0,0,0,0]
Up3=[0,0,0,0]

Gr=[0.2, 0.3, 0.4]
Gh=[0.3, 0.4, 0.5]
Gg=[0.4, 0.5, 0.7]
Gf=[0.6, 0.7, 0.8]

Sr=[1, 0.6320168586703324, 0.1242950726661382]
Sh=[1, 0.47429915389958577, 0.09949099571132]
Sg=[0.8300940153501309, 0.379404849772411, 0.0711371443304496]
Sf=[0.5539388563109415, 0.2706165505728599, 0.06375514393314223]


zetap = data.zetap
thetap = data.thetap
C = [data.c] * n
l1 = data.l1
l2 = data.l2

G=[Gr,Gh,Gg,Gf]
S=[Sr,Sh,Sg,Sf]

E = [[0,0.1,0.01],[0.1,0,0.01],[0.01,0,0.01]]

# lambd = data.lambd
# phi = data.phi
#
#
# Q = -q * np.power(g,2) + 2*q * g
# Uu1 = lambd * Q - c * g
# Uu2 = lambd * Q - (1-b) * phi * c * g - b * data.s * c * g
# Uu3 = lambd * Q - phi * c * g

for k in [0,1,2,3]:

    sump1 = 0
    sump2 = 0
    sump3 = 0
    gama1 = 0
    gama2 = 0
    gama3 = 0


    for i in range(0, n, 1):
        sume1 = 0
        sume2 = 0
        sume3 = 0

        for j in range(0, n, 1):
            if i != j:
                sume1 = sume1 + E[i][j] * 1 * G[k][i]
                sume2 = sume2 + E[i][j] * S[k][i] * G[k][i]
                sume3 = 0

        sump1 = sump1 + P[i] * 1 * G[k][i]
        sump2 = sump2 + P[i] * S[k][i] * G[k][i]
        sump3 = sump3 + P[i] * 0 * G[k][i]
        gama1 = gama1 + (1 + sume1) * data.l1 * 1 * G[k][i] + data.l2 * pow(1 * G[k][i], 2)
        gama2 = gama2 + (1 + sume2) * data.l1 * S[k][i] * G[k][i] + data.l2 * pow(S[k][i] * G[k][i], 2)
        gama3 = 0

    Vp = data.thetap * pow(sum(G[k]), data.zetap)
    Phi1 = b * sump1 + Vp
    Phi2 = b * sump2 + Vp
    Phi3 = b * sump3 + Vp
    Psi1 = data.cp  + gama1
    Psi2 = data.cp  + gama2
    Psi3 = data.cp  + gama3
    print(Vp)

    Up1[k] = Phi1-Psi1
    Up2[k] = Phi2-Psi2
    Up3[k] = Phi3-Psi3




# draw figure
# plt.rc('font', weight='bold')
# plt.rcParams['axes.linewidth'] = 2
# plt.subplots_adjust(left=0.15, right=0.97, top=0.97, bottom=0.15)

# plt.scatter(delta, nsNE, color="blue", s=8, linestyle="-")
# plt.plot(na, deltaNE, 'o:', color="red", ms=6,label="b=0.2")
plt.plot(g, Up1, '^-', color="b", ms=8, markerfacecolor='none', label="Untrusted Platform")
# plt.plot(na, deltaNE2, 'o:', color="blue", ms=8,label="$\mu=1.5$")
plt.plot(g, Up2, 'd--', color="g", ms=8, markerfacecolor='none', label="Three-party")
# plt.plot(na, deltaNE3, 'h:', color="orange", ms=8,label="$\mu=2.5$")
plt.plot(g, Up3, 'o-.', color="r", ms=8, markerfacecolor='none', label="Tusted Platform")
#plt.savefig('na VS delta')

my_xticks = ['$G_r$','$G_h$','$G_g$','$G_f$']
plt.xticks(g, my_xticks)

plt.xlabel('User\'s strategy $G$', fontsize=12)
plt.ylabel('Platform\'s utility $U_p$', fontsize=12)

# plt.ylim(10, 25.5)
# plt.grid(linewidth=0.5, linestyle=':')
plt.legend(loc=0,prop={'size':12})

#plt.xlim(0, 10)
#plt.ylim(1, 16)
#plt.xticks(np.linspace(0, 10, 6, endpoint=True),fontsize=20)
#plt.yticks(np.linspace(1, 16, 6,endpoint=True),fontsize=20)
fig = plt.gcf()
fig.set_size_inches(5, 3.2)
plt.subplots_adjust(left=0.15, right=0.9, top=0.96, bottom=0.165)


plt.show()