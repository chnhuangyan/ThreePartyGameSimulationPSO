import Data as data
import numpy as np
import matplotlib.pyplot as plt

b = data.b
g = [0,1,2,3]
Q=data.Q
C = data.C
n = 3
# s1 = 1
# s3 = 0
# s2 = [0,0,0,0,0,0,0,0,0,0,0]

C1=[0,0,0,0]
C2=[0,0,0,0]
C3=[0,0,0,0]

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

l1 = data.l1
l2 = data.l2

G=[Gr,Gh,Gg,Gf]
S=[Sr,Sh,Sg,Sf]

E = [[0,0.1,0.01],[0.1,0,0.01],[0.01,0,0.01]]

for k in g:
    sumquadra = 0
    sumc = 0

    sums1 = 0
    sums2 = 0
    for i in [0,1,2]:
        sume = 0
        for j in [0,1,2]:
            if i != j:
                sume = sume + E[i][j] * G[k][i]

        sumquadra = sumquadra + (1 + sume) * (-Q[i] * pow(G[k][i], 2) + 2 * Q[i] * G[k][i])


        sumc = sumc + C[i] * data.phi * G[k][i]

        sums1 = sums1 + C[i] * 1 * G[k][i]
        sums2 = sums2 + C[i] * S[k][i] * G[k][i]


    C1[k] = (1-b)*sumc+b*sums1
    C2[k] =(1-b)*sumc+b*sums2
    C3[k] = sumc
# for i in g:
#     # s2[i] =  min((b*p-l1)/(2*l2*n*g[i]),1)
#     for j in [0,1,2]:
# Up2[i] = b*Sg[i]*p*n*g[i]+thetap*pow(n*g[i],zetap)-cp*n-l1*Sg[i]*n*g[i]-l2*pow(s2[i]*n*g[i],2)
# Up1 = b*s1*p*n*g+thetap*pow(n*g,zetap)-cp*n-l1*s1*n*g-l2*pow(s1*n*g,2)
# Up3 = b*s3*p*n*g+thetap*pow(n*g,zetap)-cp*n-l1*s3*n*g-l2*pow(s3*n*g,2)

my_xticks = ['$G_r$','$G_h$','$G_g$','$G_f$']
plt.xticks(g, my_xticks)

# plt.scatter(delta, nsNE, color="blue", s=8, linestyle="-")
# plt.plot(na, deltaNE, 'o:', color="red", ms=6,label="b=0.2")
plt.plot(g, C1, '^-', color="b", ms=8, markerfacecolor='none', label="Untrusted Platform")
# plt.plot(na, deltaNE2, 'o:', color="blue", ms=8,label="$\mu=1.5$")
plt.plot(g, C2, 'd--', color="g", ms=8, markerfacecolor='none', label="Three-party")
# plt.plot(na, deltaNE3, 'h:', color="orange", ms=8,label="$\mu=2.5$")
plt.plot(g, C3, 'o-.', color="r", ms=8, markerfacecolor='none',  label="Trusted Platform")
#plt.savefig('na VS delta')

plt.xlabel('User\'s strategy $G$', fontsize=12)
plt.ylabel('User\'s cost', fontsize=12)

# plt.ylim(0, 5)

# plt.grid(linewidth=0.5, linestyle=':')
plt.legend(prop={'size':12})

fig = plt.gcf()
fig.set_size_inches(5, 3.2)
plt.subplots_adjust(left=0.15, right=0.9, top=0.96, bottom=0.165)

plt.show()