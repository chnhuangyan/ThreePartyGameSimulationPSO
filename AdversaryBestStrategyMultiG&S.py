import Data as data
import numpy as np
import matplotlib.pyplot as plt

b = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
g = data.g
P = data.P
n = data.n
s = data.s

x=[0,1,2,3]



Sr=[0.5, 0.7, 0.8]
Sh=[0.4, 0.6, 0.7]
Sg=[0.3, 0.5, 0.6]
Sf=[0.2, 0.4, 0.5]


Gr=[0.2, 0.3, 0.4]
Gh=[0.3, 0.4, 0.5]
Gg=[0.4, 0.5, 0.7]
Gf=[0.6, 0.7, 0.8]


zetaa = data.zetaa
thetaa = data.thetaa
cp = data.cp
l1 = data.l1
l2 = data.l2
phi = data.phi

# s1 = 0.4
# s2 = 0.6
# s3 = 0.8

sigma1 = data.sigma1
sigma2 = data.sigma2

# br = np.arange(0, 0.5, 0.1)
# bh = np.arange(0, 0.5, 0.1)
# bg = np.arange(0, 0.5, 0.1)
# bf = np.arange(0, 0.5, 0.1)

G=[Gr,Gh,Gg,Gf]
S=[Sr,Sh,Sg,Sf]

for i in x: #S
    for j in x: #G
        sums =0
        sump =0
        for k in [0,1,2]:
            sums = sums + S[i][k]*G[j][k]
            sump = sump + P[k] * S[i][k] * G[j][k]

        print('sums:',sums)
        b[i][j] = (thetaa*pow(sums, zetaa) - thetaa*pow(phi*sum(G[j]),zetaa)-sump+2*sigma1+sigma2)/(2*sigma1)
        print('b',b[i][j])
        b[i][j] = max((thetaa*pow(sums, zetaa) - thetaa*pow(phi*sum(G[j]),zetaa)-sump+2*sigma1+sigma2)/(2*sigma1),0)
        b[i][j] = min(b[i][j], 1)



    # b1[i] = max((thetaa*pow(s1*n*g[i], zetaa) - thetaa*pow(phi*n*g[i],zetaa)-p*s1*n*g[i]+2*sigma1+sigma2)/(2*sigma1),0)
    # b2[i] = max((thetaa*pow(s2*n*g[i], zetaa) - thetaa*pow(phi*n*g[i],zetaa)-p*s2*n*g[i]+2*sigma1+sigma2)/(2*sigma1),0)
    # b3[i] = max((thetaa*pow(s3*n*g[i], zetaa) - thetaa*pow(phi*n*g[i],zetaa)-p*s3*n*g[i]+2*sigma1+sigma2)/(2*sigma1),0)
    # b1[i] = min(b1[i],1)
    # b2[i] = min(b2[i],1)
    # b3[i] = min(b3[i],1)

#b1 = (thetaa*pow(s1*n*g, zetaa) - thetaa*pow(phi*n*g,zetaa)-p*s1*n*g+2*sigma1+sigma2)/(2*sigma1)
#b2 = (thetaa*pow(s2*n*g, zetaa) - thetaa*pow(phi*n*g,zetaa)-p*s2*n*g+2*sigma1+sigma2)/(2*sigma1)
#b3 = (thetaa*pow(s3*n*g, zetaa) - thetaa*pow(phi*n*g,zetaa)-p*s3*n*g+2*sigma1+sigma2)/(2*sigma1)

print(b[0])
print(b[1])
print(b[2])
print(b[3])

plt.plot(x,b[0], "^-",color='b',ms=8, markerfacecolor='none',label="$S=S_r$")
plt.plot(x,b[1], "d--",color='g',ms=8, markerfacecolor='none',label="$S=S_h$")
plt.plot(x,b[2], "o-.",color='r',ms=8, markerfacecolor='none',label="$S=S_g$")
plt.plot(x,b[3], "s:",  color='k',ms=8, markerfacecolor='none',label="$S=S_f$")


my_xticks = ['$G_r$','$G_h$','$G_g$','$G_f$']
plt.xticks(x, my_xticks)

plt.xlabel('User\'s strategy $G$', fontsize=12)
plt.ylabel('Adversary\'s optimal strategy $b^*$', fontsize=12)

# plt.grid(linewidth=0.5, linestyle=':')
plt.legend(loc = 3, prop={'size':12})
fig = plt.gcf()
fig.set_size_inches(5, 3.2)
plt.subplots_adjust(left=0.15, right=0.9, top=0.96, bottom=0.165)


plt.show()