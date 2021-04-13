import matplotlib.pyplot as plt


p1=[
0.9343,
0.9032,
0.835,
0.7945,
0.7213,
0.6543,
0.5923,
0.5292,
0.4623,
0.4123,
0.3444]

p2=[
0.8643,
0.8032,
0.7435,
0.7045,
0.6213,
0.5343,
0.4723,
0.3892,
0.2923,
0.2023,
0.1244]

p3=[
0.81,
0.7332,
0.6721,
0.6045,
0.5213,
0.4343,
0.3123,
0.2192,
0.1323,
0,
0]



s=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]


plt.plot(s,p1,"^-",color='b',ms=8, markerfacecolor='none',label="$p_1$")
plt.plot(s,p2,"d--",color='g',ms=8, markerfacecolor='none',label="$p_2$")
plt.plot(s,p3,"o-.",color='r',ms=8, markerfacecolor='none',label="$p_3$")



plt.xlabel('Selling Strategy $s$', fontsize=12)
plt.ylabel('User\'s Optimal $g$', fontsize=12)

plt.legend(loc=0,prop={'size':12})

# plt.ylim(1, 4.5)

# plt.plot(s[7],p1[7],'b^')
# plt.plot(s[6],p2[6],'gd')
# plt.plot(s[5],p3[5],'ro')

fig = plt.gcf()
fig.set_size_inches(5, 3.2)
plt.subplots_adjust(left=0.15, right=0.9, top=0.96, bottom=0.165)


plt.show()
fig.savefig('03_user_os_s_p.eps',format='eps',dpi=1000)