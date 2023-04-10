# Series
# Work by Anthony O'Neal
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def tay1(y, x):

    return (1-x)-(1/3)*x**3-(1/12)*x**4


y0 = 1
xs = np.linspace(0,5,100)
ys = odeint(tay1, y0, xs)
ys = np.array(ys).flatten()

plt.plot(xs, ys)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('taylor expansion part 1')
plt.show()

def tay2(y, x):

    return 6+(x-3)+(-11/2)*(x-3)**2

y02 = 1
xs2 = np.linspace(0,5,100)
ys2 = odeint(tay2, y02, xs2)
ys2 = np.array(ys2).flatten()

plt.plot(xs2, ys2)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('taylor expansion part 2')
plt.show()

def powerS(y, x):
    return 1*(1-(1/10)*x-(1/20)*x**2-(1/60)*x**3-(1/100)*x**4-(1/150)*x**5-(1/210)*x**6-(1/280)*x**7-(1/360)*x**8)

y03 = 1
xs3 = np.linspace(0,5,100)
ys3 = odeint(powerS, y03, xs3)
ys3 = np.array(ys3).flatten()

plt.plot(xs3, ys3)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Part 2 Power Series')
plt.show()


print("u = processing speed\n")
print("t = cpu time\n")

print("du/dt = -k*t\n")

def dudt(u, t):
    k=8
    return -k*t


xo=100
xs = np.linspace(1,5,100)
ys=odeint(dudt,xo,xs)
ys = np.array(ys).flatten()
plt.rcParams.update({'font.size': 14})  # increase the font size
plt.subplot(2,1,1)
plt.xlabel("processing speed(ghz/s)")
plt.ylabel("cpu time(clock cycles)")
plt.plot(xs, ys);
#plt.plot(xs,ys2);
plt.show()
