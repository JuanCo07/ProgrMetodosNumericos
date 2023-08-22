import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

fx = input("Ingrese la función a integrar: ")
f = lambda x: eval(fx)

a = float(input("Ingrese el límite inferior de integración: "))
b = float(input("Ingrese el límite superior de integración: "))
n = int(input("Ingrese el número de trapecios a utilizar: "))

x = np.linspace(a, b, n+1)
y = f(x)
h = (b-a)/n

if n==1:
  T = (h/2)*(y[0] + y[1])
if n>2:
  T = (h/2)*(y[0] + y[n] + 2*np.sum(y[1:n]))

real_integral = integrate.quad(f, a, b)[0]
error = abs(T - real_integral) / real_integral * 100

print("La aproximación de la solución es", T)
print("Error porcentual:", error, "%")

fig, ax = plt.subplots()
ax.plot(x, y)

for i in range(n):
    xs = [x[i], x[i+1], x[i+1], x[i]]
    ys = [0, 0, f(x[i+1]), f(x[i])]
    ax.plot(xs, ys, 'b', lw=1)

#xm = (x[:-1] + x[1:])/2
#ym = f(xm)
#for i in range(n):
#    ax.plot([xm[i], xm[i]], [0, ym[i]], 'r--', lw=1)

#Grafica
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Método del trapecio o trapezoidal')
plt.show()
