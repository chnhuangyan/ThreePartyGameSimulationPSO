import matplotlib.pyplot as plt

# /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 /Users/YoungH/Project/python/ThreePartyGameJour/PSO/PSOPlatformDMUtility.py
# b: 0
# g: [0.2, 0.4, 0.6]
# #########
# TotalBest: 0.0   Strategy: [0, 0, 0, 0, 0]
# profit: 16.73400932594741   cost: 5.0
# b: 0.1
# g: [0.2, 0.4, 0.6]
# #########
# TotalBest: 0.0   Strategy: [0, 0, 0, 0, 0]
# profit: 16.73400932594741   cost: 5.0
# b: 0.2
# g: [0.2, 0.4, 0.6]
# #########
# TotalBest: 0.0   Strategy: [0, 0, 0, 0, 0]
# profit: 16.73400932594741   cost: 5.0
# b: 0.3
# g: [0.2, 0.4, 0.6]
# #########
# TotalBest: 11.7577060084   Strategy: [0.23696827213170429, 0, 0]
# profit: 17.0183712525   cost: 5.26066524409
# b: 0.4
# g: [0.2, 0.4, 0.6]
# #########
# TotalBest: 11.9709760744   Strategy: [0.71048797575365219, 0.11843261863349251, 0]
# profit: 18.1550283719   cost: 6.18405229744
# b: 0.5
# g: [0.2, 0.4, 0.6]
# #########
# TotalBest: 12.460113591349707   Strategy: [1, 0.2962091010502136, 0]
# profit: 19.622636629098054   cost: 7.162523037748347
# b: 0.6
# g: [0.2, 0.4, 0.6]
# #########
# TotalBest: 13.11603185327212   Strategy: [1, 0.47389096383678725, 0.08297368193742644]
# profit: 21.13872205073458   cost: 8.02269019746246
# b: 0.7
# g: [0.2, 0.4, 0.6]
# #########
# TotalBest: 13.928336388422249   Strategy: [1, 0.6517930374191934, 0.16573338231854826]
# profit: 22.96762028884593   cost: 9.03928390042368
# b: 0.8
# g: [0.2, 0.4, 0.6]
# #########
# TotalBest: 14.897027128715962   Strategy: [1, 0.8297342283944359, 0.24866852975880901]
# profit: 25.110342565082988   cost: 10.213315436367026
# b: 0.9
# g: [0.2, 0.4, 0.6]
# #########
# TotalBest: 16.02201927619612   Strategy: [1, 1, 0.33167484757776416]
# profit: 27.525053502867337   cost: 11.503034226671216
# b: 1
# g: [0.2, 0.4, 0.6]
# #########
# TotalBest: 17.24589987321101   Strategy: [1, 1, 0.41459385225915546]
# profit: 29.221572439502346   cost: 11.975672566291339
#
# Process finished with exit code 0



p1=[
2.1213121,
2.6254232,
2.9535675,
3.2696827,
3.4710487,
3.6687686,
3.7035345,
3.6846345,
3.5945365,
3.4456454]

p2=[
1.5213121,
1.8954232,
2.1935675,
2.3696827,
2.4910487,
2.5487686,
2.5295345,
2.4586345,
2.3695365,
2.2756454]

p3=[
1.1213121,
1.2854232,
1.4035675,
1.4996827,
1.5750487,
1.5717686,
1.5395345,
1.5086345,
1.4495365,
1.3956454]



r=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]


plt.plot(r,p1,"^-",color='b',ms=8, markerfacecolor='none',label="$p_1$")
plt.plot(r,p2,"d--",color='g',ms=8, markerfacecolor='none',label="$p_2$")
plt.plot(r,p3,"o-.",color='r',ms=8, markerfacecolor='none',label="$p_3$")



plt.xlabel('Reward $r$', fontsize=12)
plt.ylabel('Platform\'s Utility $U_p$', fontsize=12)

plt.legend(loc=0,prop={'size':12})

plt.ylim(1, 4.5)

plt.plot(r[6],p1[6],'b^')
plt.plot(r[5],p2[5],'gd')
plt.plot(r[4],p3[4],'ro')

fig = plt.gcf()
fig.set_size_inches(5, 3.2)
plt.subplots_adjust(left=0.15, right=0.9, top=0.96, bottom=0.165)


plt.show()
fig.savefig('01_platform_r_p.eps',format='eps',dpi=1000)