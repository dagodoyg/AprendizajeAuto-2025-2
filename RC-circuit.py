import math as m
import numpy as np
import matplotlib.pyplot as plt

def C_volts(C: float, R: float, eps: float, t: float) -> float:
    return eps * ( 1 - m.exp( -t / (R*C) ) )

t = np.linspace(0,10,100)
C = float(input("C: "))
R = float(input("R: "))
eps = float(input('\u03B5: '))
v = []

for ii in range(len(t)):
    v.append(C_volts(C,R,eps,t[ii]))

plt.plot(t,v)
plt.xlabel("t")
plt.ylabel("V")
plt.show()
