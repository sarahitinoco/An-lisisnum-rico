#Ejercicio 1
import math as mt
import numpy as np
"""
f = float(input("Ingrese una temperatura en grado farenheit: "))
c = (f-32)*(1.8)
print("tu temperatura es :", c, "celsius")


#Ejercicio 2
x=5
a= mt.sinh(5)
print("el seno hiperbólico  de 5 es ", a)
e= (mt.e**x-mt.e**(-x))/2
print("la ecuación es igual a ", e)


#1
s = (mt.exp(x) - mt.exp(-x))/2
print("el resultado de la ecuación es ", s)


#2
w= 6+3j
w1= 2+4j
w2= 3j
r= w+w1 
print("el número complejo r es: ", r)

q=5
p=9
print("el resultado es: ", complex(q, p))

#Ejercicio 3
from cmath import sin, sinh, exp, e, cos
#1
X= complex(input('Ingrese un número: '))
#x1= float(X)
print('sin(i ', X, ')=', sin(X*1j))
print('sinh(', X, ')=', 1j*sinh(X))

#2
n=complex(input('Ingrese un número complejo:\n '))
ne= exp(1j*n)
print(f'su número es {ne}')
print(f'Su número con la relación coseno + seno es {cos(n)+ 1j*sin(n)}')


#Ejercicio 4
def raices(a, b, c):
    discriminante = b**2 - 4*a*c
    
    if discriminante >= 0:
        raiz1 = (-b + np.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - np.sqrt(discriminante)) / (2*a)
    else:
        raiz1 = (-b + np.sqrt(-discriminante) * 1j) / (2*a)
        raiz2 = (-b - np.sqrt(-discriminante) * 1j) / (2*a)
    
    return raiz1, raiz2

a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

raiz1, raiz2 = raices(a, b, c)

print(f"Para a={a}, b={b}, c={c}, las raíces son: {raiz1} y {raiz2}")
"""

#Ejercicio 5
def trayectoria(v_0, theta, y_0, x):
    g = 9.81  
    theta_rad = np.radians(theta)
    
    
    y = y_0 + x * np.tan(theta_rad) - (g * x**2) / (2 * v_0**2 * np.cos(theta_rad)**2)
    
    return y

v_0 = float(input("Ingresa la velocidad inicial (v_0) en m/s: "))
theta = float(input("Ingresa el ángulo de lanzamiento (θ) en grados: "))
y_0 = float(input("Ingresa la altura inicial (y_0) en metros: "))
x = float(input("Ingresa la distancia horizontal (x) en metros: "))


y = trayectoria(v_0, theta, y_0, x)

print("\nResultados:")
print(f"Trayectoria en y(x) = {y} metros")
