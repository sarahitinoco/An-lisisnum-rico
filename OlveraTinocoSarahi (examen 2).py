#Examen Análisis numérico 2
#Alumna:Sarahí Olvera Tinoco

import math
import sys 
from numpy import sign

"""
#Ejercicio 1

def err(string):
    print(string)
    input('Press return to exit')
    sys.exit()

#Método de Newton-Raphson combinado con bisección
def newtonRaphson(f, df, a, b, tol=1.0e-9):
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if sign(fa) == sign(fb): err('La raíz no está en el intervalo')
    x = 0.5 * (a + b)  
    for i in range(30):  
        fx = f(x)
        if fx == 0.0: return x  
        if sign(fa) != sign(fx): 
            b = x  
        else: 
            a = x
        dfx = df(x)
        try:
            dx = -fx / dfx  #Paso Delta X
        except ZeroDivisionError:
            dx = b - a  #Si la derivada es cero, usar bisección
        x = x + dx  
        if (b - x) * (x - a) < 0.0:  #Si el resultado está fuera del intervalo
            dx = 0.5 * (b - a)
            x = a + dx
        if abs(dx) < tol * max(abs(b), 1.0):  #Verificar la convergencia
            return x
    print('Too many iterations in Newton-Raphson')
    return None

#Definimos la función y su derivada
def f(x):
    return x**3 - 75  #Función para calcular la raíz cúbica de 75

def df(x):
    return 3 * x**2  #Derivada de la función

#Intervalos y límite de cifras
a = 4  #Límite inferior del intervalo
b = 5  #Límite superior del intervalo
lim = 1.0e-4  #Cuatro cifras significativas

#Usamos el método de Newton-Raphson
raiz = newtonRaphson(f, df, a, b, lim)
if raiz is not None:
    print(f"La raíz cúbica de 75 es aproximadamente: {raiz:.4f}")



#Ejercicio 2

# Definimos la función
def y(x):                    
    return x**3 - 3.23 * x**2 - 5.54 * x + 9.84

#Petición de datos
x1 = float(input('Captura el valor de x1: '))  
x2 = float(input('Captura el valor de x2: '))  

#Evalua la función 
y1 = y(x1)                                    
y2 = y(x2)                                    

#Checamos que los signos sean iguales, en caso de que no, arroja el mensaje de 'no hay raíces en el intervalo'
if y1 * y2 > 0:                                
    print('No hay raíces en el intervalo')
    exit()

# Método de bisección
for i in range(100):  
    xh = (x1 + x2) / 2  #Punto medio del intervalo
    yh = y(xh)          #Evalua la función y(xh)
    if abs(yh) < 1.0e-6:  #Verificamos la raíz
        break
    elif y1 * yh < 0: 
        x2 = xh           
    else: 
        x1 = xh

#Imprimimos los resultados
print('La raíz es: %.5f' % xh)
print('Número de bisecciones: %d' % (i + 1))
"""

#Ejercicio 3




"""
#Ejercicio 4

#Función a integrar
def f(x): 
    if x==0:
        return 0
    return math.sin(x) / math.sqrt(x)

def trapecio_recursiva(f, a, b, Iold, k):
    if k == 1:
        return (f(a) + f(b)) * (b - a) / 2
    else:
        n = 2**(k - 2)  
        h = (b - a) / (2**(k - 1)) 
        suma = 0.0
        for i in range(1, 2 * n, 2): 
            x = a + i * h
            suma += f(x)
        return 0.5 * Iold + h * suma

#Intervalo de integración
a = 0.0
b = 1.0

Iold = 0.0
for k in range(1, 21):
    Inew = trapecio_recursiva(f, a, b, Iold, k)
    if k > 1 and abs(Inew - Iold) < 1.0e-6:
        break
    Iold = Inew

n_panels = 2**(k - 1)

print("Integral =", round(Inew, 7))
print("n Panels =", n_panels)
"""