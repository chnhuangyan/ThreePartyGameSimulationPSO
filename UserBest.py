import Data as data
import numpy as np
import matplotlib.pyplot as plt
import math

q = data.q
n = data.n
b = data.b
c = data.c
s = data.s

s = np.arange(0, 1.1, 0.1)

b1 = 0.4
b2 = 0.6
b3 = 0.8
lambd = data.lambd
phi = data.phi

g1 = (2*lambd*q - 2*b1*c*s + 2*c*phi*(b1 - 1))/(2*c*(b1 - 1)*pow(phi,2) - 2*b1*c*pow(s,2) + 2*lambd*q)
g2 = (2*lambd*q - 2*b2*c*s + 2*c*phi*(b2 - 1))/(2*c*(b2 - 1)*pow(phi,2) - 2*b2*c*pow(s,2) + 2*lambd*q)
g3 = (2*lambd*q - 2*b3*c*s + 2*c*phi*(b3 - 1))/(2*c*(b3 - 1)*pow(phi,2) - 2*b3*c*pow(s,2) + 2*lambd*q)


# draw figure
plt.rc('font', weight='bold')
plt.rcParams['axes.linewidth'] = 2
plt.subplots_adjust(left=0.15, right=0.97, top=0.97, bottom=0.15)

# plt.scatter(delta, nsNE, color="blue", s=8, linestyle="-")
# plt.plot(na, deltaNE, 'o:', color="red", ms=6,label="b=0.2")
plt.plot(s, g1, 'd:', color="red",linewidth = 4, ms=12,markeredgewidth=4,markerfacecolor='none', label="$b=0.4$")
# plt.plot(na, deltaNE2, 'o:', color="blue", ms=8,label="$\mu=1.5$")
plt.plot(s, g2, 'v-.', color="green",linewidth = 4, ms=12,markeredgewidth=4,markerfacecolor='none', label="$b=0.6$")
# plt.plot(na, deltaNE3, 'h:', color="orange", ms=8,label="$\mu=2.5$")
plt.plot(s, g3, 'h--', color="blue",linewidth = 4, ms=12,markeredgewidth=4,markerfacecolor='none', label="$b=0.8$")
#plt.savefig('na VS delta')


plt.xlabel('Platform selling strategy $s$', fontsize=21)
plt.ylabel('Optimal granularity $g^*$', fontsize=20)

# plt.grid(linewidth=0.5, linestyle=':')
plt.legend(prop={'size':21})

#plt.xlim(0, 10)
#plt.ylim(1, 16)
#plt.xticks(np.linspace(0, 10, 6, endpoint=True),fontsize=20)
#plt.yticks(np.linspace(1, 16, 6,endpoint=True),fontsize=20)


plt.show()