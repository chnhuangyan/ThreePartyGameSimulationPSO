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
x = 10
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
S = [0.2, 0.4, 0.6]

b = data.b

# b=1

# C = [1,2,3,4,5]
#c = data.c
#s = data.s


# print(C)
# print(S)


############################

#########Functions: Valuation Compare Initialization###########

def Init():
    # print('Init')
    global G, V, pbest, gbest, t, bestV
    t = 0
    bestV = 0.0

    gbest = np.zeros(n);
    pbest = [[0] * n for i in range(x)]

    G = [([0] * n) for i in range(x)]
    V = [([0] * n) for i in range(x)]

    for i in range(0, x, 1):
        for j in range(0, n, 1):
            G[i][j] = random.uniform(0, 1)
            V[i][j] = random.uniform(-0.01,0.01)
        pbest[i] = G[i]
    UpdataGlobal()

# def Cost(args):
#     sum = 0
#     sumc = 0
#     sumcs = 0
#     for i in range(0,n,1):
#
#         temp1 = sum + args[i]
#         sum =temp1
#         temp2 = sumc + C[i] * args[i]
#         sumc = temp2
#         temp3 = sumcs + C[i] * S[i] * args[i]
#         sumcs = temp3
#
#     return data.lambd*((data.q/pow(n,2))*pow(sum,2)-((2*data.q)/n)*sum+data.q)+(1-b)*data.phi*sumc+b*sumcs

def Sum(args):
    sum = 0
    for v in args:
        sum = sum + v
    return sum

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

def Reveal(args):
    sumquadra = 0
    sumc = 0
    sums = 0
    for i in range(0, n, 1):
        sume = 0
        for j in range(0, n, 1):
            if i != j:
                sume = sume + E[i][j] * args[i]

        sumquadra = sumquadra + (1 + sume) * (-Q[i]* pow(args[i], 2) + 2 * Q[i] * args[i])
        sumc = sumc + C[i] * data.phi * args[i]
        sums = sums + C[i] * S[i] * args[i]

    profit = data.lambd * sumquadra
    cost = (1-b)*sumc+b*sums

    print("profit:", profit, "  cost:", cost)




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
    global gbest, pbest,V,G
    for i in range(0, x, 1):
        for j in range(0, n, 1):
            tempV = V[i][j] + k1 * random.uniform(0, 1)*(pbest[i][j]-G[i][j]) + k2 * random.uniform(0,1) * (gbest[j]-G[i][j])
            V[i][j] =tempV
            temp = G[i][j]+V[i][j]
            G[i][j] = temp
            if G[i][j]>1:
                G[i][j] =1;
            if G[i][j]<0:
                G[i][j]=0
        pV = U(pbest[i])
        v = U(G[i])
        if v > pV:
            pbest[i] = G[i]

#############################

S0=[0.0,0.1,0.2]
S1=[0.1,0.2,0.3]
S2=[0.2,0.3,0.4]
S3=[0.3,0.4,0.5]
S4=[0.4,0.5,0.6]
S5=[0.5,0.6,0.7]
S6=[0.6,0.7,0.8]
S7=[0.7,0.8,0.9]
S8=[0.8,0.9,1.0]

Sr=[0.5, 0.7, 0.8]
Sh=[0.4, 0.6, 0.7]
Sg=[0.3, 0.5, 0.6]
Sf=[0.2, 0.4, 0.5]



# for b in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
for S in [S0,S1,S2,S3,S4,S5,S6,S7,S8]:
# for S in [Sr,Sh,Sg,Sf]:

    print("s:",S)
    print("b:",b)

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
        # print(gbest)

        if bestV > Tbest:
            Tbest = bestV
            TG = gbest

    print("#########")
    print("TotalBest:", Tbest, "  Strategy:", TG)
    Reveal(TG)




