import math

def f(x):
    # Definir la función que se desea integrar
    return math.sqrt(5+x**3)

def simpson(a, b):
    # Método de Simpson para aproximar la integral de f en [a,b]
    h = (b - a) / (3*n)
    print(h)
    x0 = a
    x1 = a + h
    x2 = b
    suma = f(x0) + 4*f((x0+x2)/2) + f(x2)
    integral = (h) * suma
    return integral

#def error_porcentual_simpson(a, b):
    # Calcular el error porcentual en el método de Simpson
    #f4 = math.cos(b)  # cuarta derivada de f(x) = sin(x)
    #error = ((b-a)**5 / (2880)) * abs(f4) * 100
    #return error

# Ejemplo de uso
a = 5
b = 6
n= 2
integral = simpson(a, b)
#error = error_porcentual_simpson(a, b)
print("La integral aproximada es:", integral)
#print("El error porcentual es:", error, "%")