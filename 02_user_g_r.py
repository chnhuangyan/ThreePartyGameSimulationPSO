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
1.0154232,
1.9035675,
2.5768273,
2.9610487,
3.2087686,
3.2865345,
3.2796345,
3.205365,
3.1056454,
2.8678678]

r3=[
0,
0.6254232,
1.1535675,
1.5696827,
1.7710487,
1.8602302,
1.8489022,
1.8099494,
1.7412122,
1.6656454,
1.5478678]



g=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]


plt.plot(g,r1,"^-",color='b',ms=8, markerfacecolor='none',label="$r_1$")
plt.plot(g,r2,"d--",color='g',ms=8, markerfacecolor='none',label="$r_2$")
plt.plot(g,r3,"o-.",color='r',ms=8, markerfacecolor='none',label="$r_3$")



plt.xlabel('Granularity $g$', fontsize=12)
plt.ylabel('User\'s Utility $U_u$', fontsize=12)

plt.legend(loc=0,prop={'size':12})

# plt.ylim(1, 4.5)

plt.plot(g[7],r1[7],'b^')
plt.plot(g[6],r2[6],'gd')
plt.plot(g[5],r3[5],'ro')

fig = plt.gcf()
fig.set_size_inches(5, 3.2)
plt.subplots_adjust(left=0.15, right=0.9, top=0.96, bottom=0.165)


plt.show()
fig.savefig('02_user_g_r.eps',format='eps',dpi=1000)