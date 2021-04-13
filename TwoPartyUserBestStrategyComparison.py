import Data as data
import numpy as np
import matplotlib.pyplot as plt
import math

q = data.q
n = data.n
b = data.b
c = np.arange(1, 5, 0.5)
s = data.s

lambd = data.lambd
phi = data.phi

g1 = (2*lambd*q-c)/(2*lambd*q)
g2 = (-c*phi+(phi-s)*b*c+2*q*lambd)/(2*lambd*q)
g3 = (2*lambd*q-phi*c)/(2*lambd*q)

#QL = (q/np.power(n,2))*np.power(n*g,2)-(2*q/n)*(n*g)+q
#Psiu1 = lambd * QL + (1-b) * phi * c * n * g + b * s1 * c * n * g
#Psiu2 = lambd * QL + (1-b) * phi * c * n * g + b * s2 * c * n * g
#Psiu3 = lambd * QL + (1-b) * phi * c * n * g + b * s3 * c * n * g


# draw figure
# plt.rc('font', weight='bold')
# plt.rcParams['axes.linewidth'] = 2
# plt.subplots_adjust(left=0.15, right=0.97, top=0.97, bottom=0.15)

# plt.scatter(delta, nsNE, color="blue", s=8, linestyle="-")
# plt.plot(na, deltaNE, 'o:', color="red", ms=6,label="b=0.2")
plt.plot(c, g1, '^--', color="b", ms=6, label="Untrusted Platform")
# plt.plot(na, deltaNE2, 'o:', color="blue", ms=8,label="$\mu=1.5$")
plt.plot(c, g2, 'd--', color="g", ms=6, label="Three-Party")
# plt.plot(na, deltaNE3, 'h:', color="orange", ms=8,label="$\mu=2.5$")
plt.plot(c, g3, 'o--', color="r", ms=6, label="Tusted Platform")
#plt.savefig('na VS delta')


plt.xlabel('User attribute unit cost $c_1$', fontsize=16)
plt.ylabel('User best granularity', fontsize=16)

# plt.grid(linewidth=0.5, linestyle=':')
plt.legend(prop={'size':12})

#plt.xlim(0, 10)
#plt.ylim(1, 16)
#plt.xticks(np.linspace(0, 10, 6, endpoint=True),fontsize=20)
#plt.yticks(np.linspace(1, 16, 6,endpoint=True),fontsize=20)


plt.show()