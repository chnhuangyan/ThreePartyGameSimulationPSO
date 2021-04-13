import Data as data
n=3

l1=data.l1
l2=data.l2
b=data.b
# g = [data.g]*n
# g = [0.6]*n
# s=[0.2,0.2,0.2,0.2,0.2]
thetap = data.thetap
zetap = data.zetap
cp=data.cp
E = [[0,0.1,0.01],[0.1,0,0.01],[0.01,0,0.01]]
Q = data.Q
P = data.P

def Up(args):
    sump = 0
    gama = 0
    sumquadra = 1

    for i in range(0, n, 1):
        sume = 0
        for j in range(0, n, 1):
            if i != j:
                sume = sume + E[i][j] * args[i] * g[i]

        # sume = sume + E[i][j] * args[i]
        # sumquadra = sumquadra + (1 + sume) * (-Q[i] * pow(g[i], 2) + 2 * Q[i] * g[i])
        sump = sump + P[i] * args[i] * g[i]
        gama = gama + (1 + sume) * data.l1 * args[i] * g[i] + data.l2 * pow(args[i] * g[i], 2)

    Vp = data.thetap * pow(sum(g), data.zetap)

    Phi = b * sump + Vp
    Psi = data.cp * sumquadra + gama

    Up = Phi - Psi

    return Up


Gr=[0.2, 0.3, 0.4]
Gh=[0.3, 0.4, 0.5]
Gg=[0.4, 0.5, 0.7]
Gf=[0.6, 0.7, 0.8]


S0=[0.0,0.1,0.2]
S1=[0.1,0.2,0.3]
S2=[0.2,0.3,0.4]
S3=[0.3,0.4,0.5]
S4=[0.4,0.5,0.6]
S5=[0.5,0.6,0.7]
S6=[0.6,0.7,0.8]
S7=[0.7,0.8,0.9]
S8=[0.8,0.9,1.0]



for g in [Gr,Gh,Gg,Gf]:
    print("g:", g)
    print("b:", b)
    for S in [S0,S1,S2,S3,S4,S5,S6,S7,S8]:
        print("S:",S)
        print("Utility:", Up(S))
