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

# C = [10] * n
# C = [1,5,10,15,20]
# C = [1,10,20,40,80]
# S = [data.s] * n
E = [[0,0.1,0.01],[0.1,0,0.01],[0.01,0,0.01]]
# g = [data.g]*n
# g = [0.1, 0.2, 0.3, 0.4, 0.5]
g= [0.2, 0.4, 0.6]
p=data.P
Q=data.Q
# p=[15, 20, 25, 30, 35]
# b=data.b
b=0.6

#C = [1,5,10,20,30]
#c = data.c
#s = data.s


# print(C)


############################

#########Functions: Valuation Compare Initialization###########

def Init():
    # print('Init')
    global S, V, pbest, gbest, t, bestV
    t = 0
    bestV = 0.0

    gbest = np.zeros(n);
    pbest = [[0] * n for i in range(x)]

    S = [([0] * n) for i in range(x)]
    V = [([0] * n) for i in range(x)]

    for i in range(0, x, 1):
        for j in range(0, n, 1):
            S[i][j] = random.uniform(0, 1)
            V[i][j] = random.uniform(-0.01,0.01)
        pbest[i] = S[i]
    UpdataGlobal()


def U(args):
    sump = 0
    gama = 0
    sumquadra = 1

    for i in range(0,n,1):
        sume = 0
        for j in range(0, n, 1):
            if i != j:
                sume = sume + E[i][j] * args[i] * g[i]

        # sumquadra = sumquadra + (1 + sume) * (-Q[i] * pow(g[i], 2) + 2 * Q[i] * g[i])
        sump = sump + p[i]*args[i]*g[i]
        gama = gama + (1+sume)*data.l1*args[i]*g[i]+data.l2*pow(args[i]*g[i],2)


    Vp=data.thetap*pow(sum(g),data.zetap)
    Phi = b*sump+Vp
    Psi = data.cp * sumquadra + gama

    return Phi - Psi

def Reveal(args):
    sump = 0
    gama = 0

    for i in range(0, n, 1):
        sume = 0
        sumquadra = 1
        for j in range(0, n, 1):
            if i != j:
                sume = sume + E[i][j] * args[i] * g[i]

        # sumquadra = sumquadra + (1 + sume) * (-Q[i] * pow(g[i], 2) + 2 * Q[i] * g[i])
        sump = sump + p[i] * args[i] * g[i]
        gama = gama + (1 + sume) * data.l1 * args[i] * g[i] + data.l2 * pow(args[i] * g[i], 2)

    Vp = data.thetap * pow(sum(g), data.zetap)
    Phi = b * sump + Vp
    Psi = data.cp * sumquadra + gama

    print("profit:", Phi, "  cost:", Psi)


def UpdataGlobal():
    #print('UpdateGlobal')
    for i in range(0,x,1):
        global gbest,bestV,pbest
        pV = U(pbest[i])
        gV = U(gbest)
        if gV < pV:
            gbest = pbest[i].copy()
            bestV = pV

            # print("gbest",gbest)
            # print('********')
            # print("G",G)
            # print('********')
            # print("V",V)
            # print('********')

            # print(bestV,t)
            #print('********')
            #print('')

def UpdataStrategy():
    #print('UpdataStrategy')
    global gbest, pbest,V,S
    for i in range(0, x, 1):
        for j in range(0, n, 1):
            tempV = V[i][j] + k1 * random.uniform(0, 1)*(pbest[i][j]-S[i][j]) + k2 * random.uniform(0,1) * (gbest[j]-S[i][j])
            V[i][j] =tempV
            temp = S[i][j]+V[i][j]
            S[i][j] = temp
            if S[i][j]>1:
                S[i][j] =1;
            if S[i][j]<0:
                S[i][j]=0
        pV = U(pbest[i])
        v = U(S[i])
        if v > pV:
            pbest[i] = S[i]


#############################

G0=[0.0,0.1,0.2]
G1=[0.1,0.2,0.3]
G2=[0.2,0.3,0.4]
G3=[0.3,0.4,0.5]
G4=[0.4,0.5,0.6]
G5=[0.5,0.6,0.7]
G6=[0.6,0.7,0.8]
G7=[0.7,0.8,0.9]
G8=[0.8,0.9,1.0]

Gr=[0.2, 0.3, 0.4]
Gh=[0.3, 0.4, 0.5]
Gg=[0.4, 0.5, 0.7]
Gf=[0.6, 0.7, 0.8]

for g in [G0,G1,G2,G3,G4,G5,G6,G7,G8]:
# for b in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
# for g in [Gr,Gh,Gg,Gf]:

    print("b:", b)
    print("g:",g)
    iteration = 0
    iteration_limit = 10
    Tbest = 0.0
    TG = [0, 0, 0, 0, 0]

    while iteration < iteration_limit:
        iteration = iteration + 1
        # print(iteration)
        # print("#########")

        Init()

        while t < 10000:
            t = t + 1
            UpdataStrategy()
            UpdataGlobal()

        # print(bestV, t)

        # TotalSbest = TotalSbest + bestV
        # print("#########")
        # print('       ')
        # print(gbest)

        if bestV > Tbest:
            Tbest = bestV
            TG = gbest

    print("#########")
    print("TotalBest:", Tbest, "  Strategy:", TG)
    Reveal(TG)


