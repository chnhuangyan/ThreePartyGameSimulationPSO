from time import sleep
from threading import Thread
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import random as random
import Data as data
import math


############################
#####Parameters for PSO#####;

# Particle number
x = 5
# dimension
n = 3
# coefficient
k1 = 0.01
k2 = 0.01

C = data.C
Q = data.Q
# C = [1,5,10,15,20]
# C = [1,10,20,40,80]
# S = [data.s] * n
E = [[0,0.1,0.01],[0.1,0,0.01],[0.01,0,0.01]]
# S = [0, 0.1, 0.2, 0.3, 0.4]

b = data.b

#C = [1,5,10,20,30]
#c = data.c
#s = data.s


print(C)
# print(S)
# arg = [1, 0.97689228194378552, 0, 0, 0]


def U(args):

    sumquadra = 0
    sumc = 0
    sums = 0

    for i in range(0,n,1):
        sume = 0
        for j in range(0,n,1):
            if i!=j :
                sume = sume + E[i][j]*args[i]

        sumquadra = sumquadra + (1+sume)*(-Q[i]*pow(args[i],2)+2*Q[i]*args[i])
        sumc = sumc + C[i]*data.phi*args[i]
        sums = sums + C[i]*S[i]*args[i]

    return data.lambd * sumquadra-(1-b)*sumc-b*sums

Sr=[0.5, 0.7, 0.8]
Sh=[0.4, 0.6, 0.7]
Sg=[0.3, 0.5, 0.6]
Sf=[0.2, 0.4, 0.5]


# Gr=[0.2, 0.3, 0.4]
# Gh=[0.3, 0.4, 0.5]
# Gg=[0.4, 0.5, 0.7]
# Gf=[0.6, 0.7, 0.8]

G0=[0.0,0.1,0.2]
G1=[0.1,0.2,0.3]
G2=[0.2,0.3,0.4]
G3=[0.3,0.4,0.5]
G4=[0.4,0.5,0.6]
G5=[0.5,0.6,0.7]
G6=[0.6,0.7,0.8]
G7=[0.7,0.8,0.9]
G8=[0.8,0.9,1.0]



for S in [Sr,Sh,Sg,Sf]:
    print()
    print()
    print("S:",S)
    for g in [G0,G1,G2,G3,G4,G5,G6,G7,G8]:
    # for g in [Gr,Gh,Gg,Gf]:
        print("g:",g)
        print("Utility:", U(g))