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
n = 5
# coefficient
k1 = 0.01
k2 = 0.01

# C = [10] * n
# C = [1,5,10,15,20]
# C = [1,10,20,40,80]
# S = [data.s] * n
E = [0.01]*n
g = [0.1, 0.2, 0.3, 0.4, 0.5]
# g = [data.g]*n
p=[data.p]*n
# p=[20, 25, 30, 35, 40]

#C = [1,5,10,20,30]
#c = data.c
#s = data.s


# print(C)


############################

#########Functions: Valuation Compare Initialization###########

def Init():
    print('Init')
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
#     return data.lambd*((data.q/pow(n,2))*pow(sum,2)-((2*data.q)/n)*sum+data.q)+(1-data.b)*data.phi*sumc+data.b*sumcs


def U(args):
    sums = 0
    sump = 0

    for i in range(0,n,1):
        sums = sums + args[i]*g[i]
        sump = sump + p[i]*args[i]*g[i]

    Vp=data.thetap*pow(sum(g),data.zetap)
    P=sump
    Phi = data.b*P+Vp
    gama = data.l1*sums+data.l2*pow(sums,2)
    Psi = data.cp*n+gama

    return Phi - Psi

# def Cost(args):
#     sum = 0
#     sumc = 0
#     sumcs = 0
#     sume = 0
#     N = n*data.e + Sum(ei)
#
#     for i in range(0,n,1):
#
#         temp1 = sum + args[i]
#         sum =temp1
#         temp2 = sumc + C[i] * args[i]
#         sumc = temp2
#         temp3 = sumcs + C[i] * S[i] * args[i]
#         sumcs = temp3
#
#         tempe = sume + ei[i]*args[i]
#         sume = tempe
#
#     return data.lambd*((data.q/pow(N,2))*pow(data.e*sum+sume,2)-((2*data.q)/N)*(data.e*sum+sume)+data.q)+(1-data.b)*data.phi*sumc+data.b*sumcs

# def Cost(args):
#     sum = 0
#     sumc = 0
#     sumcs = 0
#     sumeEaves = 0
#     sumeSell = 0
#     N = n * data.e + Sum(ei)
#
#     for i in range(0, n, 1):
#         temp1 = sum + args[i]
#         sum = temp1
#
#         temp2 = sumc + math.log(C[i] * data.phi * args[i]+1, math.e)
#         sumc = temp2
#
#         temp3 = sumcs + math.log(C[i] * S[i] * args[i]+1, math.e)
#         sumcs = temp3
#
#         tempeEaves = sumeEaves + ei[i] * data.phi * args[i]
#         sumeEaves = tempeEaves
#
#         tempeSell = sumeSell + ei[i] * S[i] * args[i]
#         sumeSell = tempeSell
#
#     eavesdropCost = (1 - data.b) * (1 + sumeEaves) * sumc
#     sellCost = data.b * (1 + sumeSell) * sumcs
#
#     ql = (data.q / pow(N, 2)) * pow(data.e * sum, 2) - ((2 * data.q) / N) * (data.e * sum) + data.q
#
#     return data.lambd * (ql) + eavesdropCost + sellCost

# def Cost(args):
#     sum = 0
#     sumc = 0
#     sumcs = 0
#
#
#     for i in range(0, n, 1):
#         temp1 = sum + args[i]
#         sum = temp1
#
#         temp2 = sumc + math.log(C[i] * data.phi * args[i]+1, math.e)
#         sumc = temp2
#
#         temp3 = sumcs + math.log(C[i] * S[i] * args[i]+1, math.e)
#         sumcs = temp3
#
#     eavesdropCost = (1 - data.b) * sumc
#     sellCost = data.b * sumcs
#
#     ql = (data.q / pow(n, 2)) * pow(sum, 2) - ((2 * data.q) / n) * sum + data.q
#
#     return data.lambd * (ql) + eavesdropCost + sellCost

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

iteration = 0
iteration_limit=10
TotalSbest = 0.0
AverageBest = 0.0

while iteration < iteration_limit:
    iteration = iteration +1
    print(iteration)
    print("#########")

    Init()

    while t<100000:

        t = t + 1
        UpdataStrategy()
        UpdataGlobal()

    print(bestV, t)

    TotalSbest = TotalSbest + bestV
    print("#########")
    print('       ')
    print(gbest)

print(TotalSbest)
AverageBest = TotalSbest/(iteration_limit)
print(AverageBest)

print("#########")

