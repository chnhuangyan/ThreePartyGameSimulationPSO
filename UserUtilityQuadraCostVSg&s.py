import Data as data
import numpy as np
import matplotlib.pyplot as plt
import math

q = data.q
g = np.arange(0, 1.1, 0.1)
c = data.c
b = data.b

zetau = 0.5

s1 = 0.4
s2 = 0.6
s3 = 0.8
lambd = data.lambd
phi = data.phi


Q = -q * pow(g,2) + 2*q * g
Uu1 = lambd * Q - (1-b)*(-c*pow(phi*g,2)+2*c*phi*g)-b*(-c*pow(s1*g,2)+2*c*s1*g)
Uu2 = lambd * Q - (1-b)*(-c*pow(phi*g,2)+2*c*phi*g)-b*(-c*pow(s2*g,2)+2*c*s2*g)
Uu3 = lambd * Q - (1-b)*(-c*pow(phi*g,2)+2*c*phi*g)-b*(-c*pow(s3*g,2)+2*c*s3*g)


# draw figure
plt.rc('font', weight='bold')
plt.rcParams['axes.linewidth'] = 2
plt.subplots_adjust(left=0.15, right=0.97, top=0.97, bottom=0.15)

# plt.scatter(delta, nsNE, color="blue", s=8, linestyle="-")
# plt.plot(na, deltaNE, 'o:', color="red", ms=6,label="b=0.2")
plt.plot(g, Uu1, 'd:', color="red",linewidth = 4, ms=12,markeredgewidth=4,markerfacecolor='none', label="$s=0.4$")
# plt.plot(na, deltaNE2, 'o:', color="blue", ms=8,label="$\mu=1.5$")
plt.plot(g, Uu2, 'v-.', color="green",linewidth = 4, ms=12,markeredgewidth=4,markerfacecolor='none', label="$s=0.6$")
# plt.plot(na, deltaNE3, 'h:', color="orange", ms=8,label="$\mu=2.5$")
plt.plot(g, Uu3, 'h--', color="blue",linewidth = 4, ms=12,markeredgewidth=4,markerfacecolor='none', label="$s=0.8$")
#plt.savefig('na VS delta')


plt.xlabel('User granularity $g$', fontsize=21)
plt.ylabel('User utility $U_u$', fontsize=21)

# plt.grid(linewidth=0.5, linestyle=':')
plt.legend(prop={'size':21})

#plt.xlim(0, 10)
#plt.ylim(1, 16)
#plt.xticks(np.linspace(0, 10, 6, endpoint=True),fontsize=20)
#plt.yticks(np.linspace(1, 16, 6,endpoint=True),fontsize=20)


plt.show()