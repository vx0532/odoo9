import matplotlib.pyplot as plt
#from bokeh.plotting.figure import figure
x1=[2*i for i in range(3,10)]
x2=[2*i for i in range(1,13)]
x3=[2*i for i in range(1,8)]
y1=[0.55,0.67,0.68,0.72,0.72,0.71,0.77]
y2=[0.08,0.12,0.12,0.2,0.21,0.23,0.19,0.2,0.21,0.23,0.23,0.24]
y3=[0,0,0.04,0.04,0.05,0.05,0.05]
fig=plt.figure()
ax=fig.add_subplot(111)
#ax1    = fig.add_axes([0.1, 0.1, 0.2, 0.2])
L1,=ax.plot(x1,y1,linewidth=2,color='r',label='1st')
ax.plot(x1,y1,'k*')
L2,=ax.plot(x2,y2,linewidth=2,color='g',label='2nd')
ax.plot(x2,y2,'k*')
ax.axis([0,25,0,0.8])
plt.grid(True)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks(x2)
xlabel=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th']
ax.xaxis.set_ticklabels(xlabel)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

axc=ax.twinx()
L3,=axc.plot(x3,y3,linewidth=2,color='b',label='3th')
axc.plot(x3,y3,'k*')
axc.axis([0,25,-0.045,0.115])
#plt.sca(ax1)   ❷ # 选择图表2的子图1
#plt.plot(x, np.sin(i*x))

plt.xlabel('Time / h')
plt.ylabel('Content / %')
plt.title('CS / Dry net ')
#plt.yticks(yticks, cluster_labels + 1)
plt.legend([L1,L2,L3], ['1st', '2nd','3rd'])
#axc.yaxis.set_ticks(-0.45,0.115)
#ax.legend(loc='best')
#plt.xticks(x2)
#line_up, = plt.plot([1,2,3], label='Line 2')
#line_down, = plt.plot([3,2,1], label='Line 1')
#plt.legend([line_up, line_down], ['Line Up', 'Line Down'])
plt.show()
plt.savefig('/home/caofa/xx.png')

from matplotlib.finance import candlestick_ohlc as candle

'''
f,axarr=plt.subplots(nrows=2,ncols=2,
        sharex='col',sharey='row',figsize=(7,5))
axarr[0,0].scatter(X,Y,c='blue',marker='^',s=50)

plt.plot(X_fit,y_lin_fit,label='linear (d=1), $R^2=%.2f$'
         %linear_r2,color='blue',lw=2)
plt.ylabel('$\sqrt{ Price \; in \; \$1000\'s [MEDV]}$')
'''