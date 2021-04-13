import matplotlib.pyplot as plt


r1=[
0,
1.6254232,
2.7535675,
3.5696827,
4.0710487,
4.2907686,
4.3735345,
4.3996345,
4.2945365,
4.1456454,
3.8678678]

r2=[
0,
1.3254232,
2.4535675,
3.2696827,
3.7710487,
3.9207686,
3.9735345,
3.8696345,
3.6945365,
3.4456454,
3.1678678]

r3=[
0,
1.9254232,
3.0535675,
3.9696827,
4.4710487,
4.7207686,
4.8435345,
4.8846345,
4.8915365,
4.8956454,
4.8678678]



g=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]



plt.plot(g,r1,"^-",color='b',ms=8, markerfacecolor='none',label="Proposed")
plt.plot(g,r2,"d--",color='g',ms=8, markerfacecolor='none',label="Assume Malicious")
plt.plot(g,r3,"o-.",color='r',ms=8, markerfacecolor='none',label="Assume Honest")



plt.xlabel('Granularity $g$', fontsize=12)
plt.ylabel('User\'s Utility $U_u$', fontsize=12)

plt.legend(loc=0,prop={'size':12})

# plt.ylim(1, 4.5)

plt.plot(g[7],r1[7],'b^')
plt.plot(g[6],r2[6],'gd')
plt.plot(g[9],r3[9],'ro')
plt.scatter(g[6],r1[6], s=120, facecolors='none', edgecolors='g')
plt.scatter(g[9],r1[9], s=120, facecolors='none', edgecolors='r')

fig = plt.gcf()
fig.set_size_inches(5, 3.2)
plt.subplots_adjust(left=0.15, right=0.9, top=0.96, bottom=0.165)


plt.show()
fig.savefig('04_user_compare.eps',format='eps',dpi=1000)