from pylab import *
import numpy

#-----------
# Section 1
# Ohm's law
#-----------

# Sample data (not from a real experiment)
from random import random
V=numpy.linspace(0,10)
G=.8 
I=numpy.zeros(len(V))
for i in range(1,len(V)):
    I[i]=G*V[i]+(.1*random())*G*V[len(V)/2.]

with open('ohm1.npy','w') as f:
    numpy.save(f,numpy.array([V,I]))

# Tasks:
# (1) Load data using built-in numpy load
#    (a) with ... as statement
#    (b) numpy arrays
#    (c) array 'slicing'
with open('ohm1.npy','r') as f:
    ohm1=np.load(f)

print ohm1
print ohm1[0,:]
print ohm1[1,:]

# (2) Basic plotting with pylab.plot (matplotlib.plot)
#    (a) basic line properties
#    (b) line width, more advanced colors
#    (c) axes labels, title, and legend
plot(ohm1[0,:],ohm1[1,:],'.y-',lw=.75,label='First example')
xlabel('Voltage')
ylabel('Current')
title("Ohm's law")
legend(loc='lower right')

#    (d) Larger font size
plot(ohm1[0,:],ohm1[1,:],'ob-',lw=1,
     label='First example')
xlabel('Voltage',fontsize=18)
ylabel('Current',fontsize=18)
title("Ohm's law",fontsize=22)
legend(loc='lower right',fontsize=18)

#    (d) xticks and yticks
xticks(fontsize=18)
yticks(np.arange(0,10,2),fontsize=18)

# (3) Trendline using polyfit
#    (a) numpy polyfit and polyval functions
#    (b) writing text on plots
#    (c) using the % trick
polynomial = np.polyfit(ohm1[0,:],ohm1[1,:],1)
print polynomial
pylab.plot(ohm1[0,:],numpy.polyval(polynomial,ohm1[0,:]),
           '--k',lw=1.5,label='linear fit')
legend(loc='lower right',fontsize=18)


#-----------
# Section 2
# Projectile motion
#-----------

# (1) figures are python objects
# (2) use figure to control size
# (3) simple subplots
# (4) using axes to make inset

accel=-9.8
x0=1.5
v0=35
t=np.linspace(0,8,100)
x=np.zeros(len(t))
v=np.zeros(len(t))
for i in range(len(t)):
    v[i]=v0+accel*t[i]
    x[i]=x0+v0*t[i]+.5*accel*t[i]**2

with open('projectile.npy','w') as f:
    numpy.save(f,numpy.array([t,v,x]))


with open('projectile.npy','r') as f:
    data=np.load(f)

t=data[0,:]
v=data[1,:]
x=data[2,:]
a=-9.8*np.ones(len(t))


f1=figure(1,(5,9))

aplt=subplot(311)
plot(t,a)
xlabel('time (s)')
ylabel('acceleration (m/s^2)')

subplot(312)
plot(t,v)
xlabel('time (s)')
ylabel('Speed (m/s)')

subplot(313)
plot(t,x)
xlabel('time (s)')
ylabel('Position (m)')




figure(2)

main=axes([.15,.15,.8,.8])
plot(t,x)
xlabel('t',fontsize=20)
ylabel('x',fontsize=20)
xticks(fontsize=18)
yticks(fontsize=18)

inset=axes([.75,.8,.18,.125])
plot(t,v)
xlabel('t',fontsize=20)
ylabel('v',fontsize=20)
xticks(fontsize=18)
yticks(arange(-50,100,50),fontsize=18)

# try again
clf()
main=axes([.15,.15,.8,.8])
plot(t,x)
xlabel('t',fontsize=20)
ylabel('x',fontsize=20)
xticks(fontsize=18)
yticks(fontsize=18)

inset=axes([.26,.24,.18,.125])
plot(t,v)
xlabel('t',fontsize=20)
ylabel('v',fontsize=20)
xticks(fontsize=18)
yticks(arange(-50,100,50),fontsize=18)


#-----------
# Section 3
# Electric field
#-----------

# (1) contour plots

x=np.linspace(-1,1,51)
y=np.linspace(-1,1,53)
E=np.zeros((len(x),len(y)))

k=[1,1]
for i in range(len(x)):
    for j in range(len(y)):
        E[i,j]=cos(2*pi*(k[0]*x[i]+k[1]*y[j]))

figure(1,(8,4))
subplot(121)
contour(x,y,E.T)

subplot(122)
contourf(x,y,E.T)


# (2) wave interference

E=np.zeros((len(x),len(y)))
k=[1,1]
for k in [[0,1],[.5,-1],[.5,.5]]:
    for i in range(len(x)):
        for j in range(len(y)):
            E[i,j]=E[i,j]+cos(2*pi*(k[0]*x[i]+k[1]*y[j]))

contourf(x,y,E.T,cmap=cm.gist_earth)
xticks(fontsize=18)
yticks(fontsize=18)
