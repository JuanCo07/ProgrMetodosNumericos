# Método de Newton-Raphson

import numpy as np
import matplotlib.pyplot as plt

# INGRESO
fx  = lambda x: x**3 + 2*(x**2) + 10*x - 20
x = np.linspace(-10,10,1000)
x1=0
error = 0.001

# PROCEDIMIENTO
tabla = []
deltax = 0.002
xi = 6
tabla.append([0,0,0])
tabla.append([x1,x1,x1])
print('Deltax',deltax)
while (error<deltax):
    xnuevo = xi -  fx(xi)*(xi-x1)/(fx(xi)-fx(x1))
    deltax = abs(xnuevo-xi)
    tabla.append([xi,xnuevo,deltax])
    plt.plot(x1,fx(x1),'ro')
    plt.plot(xi,fx(xi),'go')
    x1=xi
    xi = xnuevo
    plt.plot([xi, x1], [fx(xi), fx(x1)], color='black')
    print('Deltax',deltax)

# convierte la lista a un arreglo.
tabla = np.array(tabla)
n = len(tabla)
fi = fx(x)
# SALIDA
print(['xi', 'xnuevo', 'deltax'])
np.set_printoptions(precision = 4)
np.set_printoptions(suppress=True)
print(tabla)
print('raiz en: ', xi)
print('con error de: ',deltax)
plt.plot(x,fi,'b')
plt.plot(x1,fx(x1),'ro')
plt.plot(xi,fx(xi),'bo')
plt.axvline(x=0, ymin=-10, ymax=10)
plt.axhline(y=0, xmin=-10, xmax=10)
plt.grid()
plt.show()
