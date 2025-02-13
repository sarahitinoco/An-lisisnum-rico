#Ejercicio 1
import math as mt

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
