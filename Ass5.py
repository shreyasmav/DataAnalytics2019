
from pandas import read_csv
from matplotlib import pyplot
from matplotlib.pyplot import plot
import random
from matplotlib.pyplot import figure
figure(num=None, figsize=(10, 9), dpi=80, facecolor='w', edgecolor='k')
s = read_csv('ass5.csv', header=0, index_col=0)

r = dict()
# MOVING AVERAGE


rolling_mean = []
rolling_mean.append(s.ssp[0])
sum1 = 0
s.index[0]
for i in range(len(s)-1):
    sum1 += s.ssp[i]
    rolling_mean.append((sum1/(i+1)))
    



plot(s.index, s.ssp)
plot(s.index, rolling_mean, color='red')
pyplot.show()


r1 = 0
for i in range(1,len(rolling_mean)):
    r1 += (rolling_mean[i]-s.ssp[i])**2

r1 = r1**0.5
r1 = r1/(len(rolling_mean)-1)


print(r1)
print()
print()
print()
r["moving average"] = r1





# WEIGHTED MOVING AVERAGE


Weight = [random.random() for i in range(len(s.index))]
w = [i*len(s.index)/sum(Weight) for i in Weight]

rolling_mean = []
rolling_mean.append(s.ssp[0])
sum1 = 0
s.index[0]
for i in range(len(s)-1):
    sum1 += w[i]*s.ssp[i]
    rolling_mean.append((sum1))
    


figure(num=None, figsize=(10, 9), dpi=80, facecolor='w', edgecolor='k')

plot(s.index, s.ssp)
plot(s.index, rolling_mean, color='red')
pyplot.show()


r1 = 0
for i in range(1,len(rolling_mean)):
    r1 += (rolling_mean[i]-s.ssp[i])**2

r1 = r1**0.5
r1 = r1/(len(rolling_mean)-1)
print(r1)
r["weighted moving average"] = r1
print()
print()
print()

# SIMPLE EXPONENTIAL SMOOTHING


def sms(s,d,alpha,t):
    if(t==0):
        return d
    d = sms(s,d,alpha,t-1)
    d.append(alpha*s[t]+ (1-alpha)*d[t-1])
    return d

print("alpha = ", 0.2)

rolling_mean = []
rolling_mean.append(s.ssp[0])

rolling_mean = sms(s.ssp,rolling_mean,0.2,len(s.index)-1)
figure(num=None, figsize=(10, 9), dpi=80, facecolor='w', edgecolor='k')
   
plot(s.index, s.ssp)
plot(s.index, rolling_mean, color='red')
pyplot.show()

r1 = 0
for i in range(1,len(rolling_mean)):
    r1 += (rolling_mean[i]-s.ssp[i])**2

r1 = r1**0.5
r1 = r1/(len(rolling_mean)-1)
r["simple es 0.2"] = r1

print(r1)
print()
print()
print()

print("alpha = ", 0.4)
rolling_mean = []
rolling_mean.append(0)

rolling_mean = sms(s.ssp,rolling_mean,0.4,len(s.index)-1)
figure(num=None, figsize=(10, 9), dpi=80, facecolor='w', edgecolor='k')
  
plot(s.index, s.ssp)
plot(s.index, rolling_mean, color='red')
pyplot.show()

r1 = 0
for i in range(1,len(rolling_mean)):
    r1 += (rolling_mean[i]-s.ssp[i])**2

r1 = r1**0.5
r1 = r1/(len(rolling_mean)-1)


print(r1)
r["simple es 0.4"] = r1
print()
print()
print()
print("alpha = ", 0.6)
rolling_mean = []
rolling_mean.append(s.ssp[0])

rolling_mean = sms(s.ssp,rolling_mean,0.6,len(s.index)-1)
figure(num=None, figsize=(10, 9), dpi=80, facecolor='w', edgecolor='k')
  
plot(s.index, s.ssp)
plot(s.index, rolling_mean, color='red')
pyplot.show()

r1 = 0
for i in range(1,len(rolling_mean)):
    r1 += (rolling_mean[i]-s.ssp[i])**2

r1 = r1**0.5
r1 = r1/(len(rolling_mean)-1)


print(r1)
print()
print()
print()
r["simple es 0.6"] = r1
print("alpha = ", 0.8)
rolling_mean = []
rolling_mean.append(s.ssp[0])

rolling_mean = sms(s.ssp,rolling_mean,0.8,len(s.index)-1)
figure(num=None, figsize=(10, 9), dpi=80, facecolor='w', edgecolor='k')
 
plot(s.index, s.ssp)
plot(s.index, rolling_mean, color='red')
pyplot.show()

r1 = 0
for i in range(1,len(rolling_mean)):
    r1 += (rolling_mean[i]-s.ssp[i])**2

r1 = r1**0.5
r1 = r1/(len(rolling_mean)-1)

r["simple es 0.8"] = r1
print(r1)
print()
print()
print()
#DOUBLE EXPONENTAIL SMOOTHING




def dsms(s,b,d,f,alpha,beta,t):
    if t == 0:
        return b,d,f
    b,d,f = dsms(s,b,d,f,alpha,beta,t-1)
    b.append(alpha*s[t] + (1-alpha)*f[t])
    d.append(beta*(s[t]-s[t-1]) + (1-beta)*d[t-1])
    f.append(s[t]+d[t])
    return b,d,f



def doublees(s,alpha,beta,r):

    print("alpha = ", alpha, ", beta = ", beta)
    
    d = []
    d.append(s.ssp[0])
    
    
    d2 = []
    d2.append((s.ssp[len(s.index)-1] - s.ssp[0])/len(s.index))
    
    rolling_mean = []
    rolling_mean.append(s.ssp[0])
    rolling_mean.append(d[0]+d2[0])
    
    d,d2,rolling_mean = dsms(s.ssp,d,d2,rolling_mean,alpha,beta,len(s.index)-1)
    
    rolling_mean = rolling_mean[1:]
    
    '''for i in range(1,len(s.index)):
        rolling_mean.append(d[i]+i*d2[i])
    '''
    figure(num=None, figsize=(10, 9), dpi=80, facecolor='w', edgecolor='k')

    plot(s.index, s.ssp)
    plot(s.index, rolling_mean, color='red')
    pyplot.show()
    
    r1 = 0
    for i in range(1,len(rolling_mean)):
        r1 += (rolling_mean[i]-s.ssp[i])**2
    
    r1 = r1**0.5
    r1 = r1/(len(rolling_mean)-1)
    
    
    print(r1)
    r["double es a = "+str(alpha)+" b = "+str(beta)] = r1
    print()
    print()
    print()


alpha = [0.2,0.4,0.6,0.8]

beta = [0.2,0.4,0.6,0.8]

for i in alpha:
    for j in beta:
        doublees(s,i,j,r)



for i in r:
    print(i," : ",r[i])