#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tarea 1 
IF4702 - Física Computacional I
María Fernanda Quesada Mena
"""
# Calcular del desplazamiento de una función por integración 
# numérica, aplicando el método de Newton-Cotes Simpson 1/3

# se define la función a integrar
def F(t):
    valorF = (0.5 + 0.005*t)
    return valorF

# se definen los límites de integración a y b
a = 0.0
b = 100.0

# se establece el número de puntos para el cálculo numérico
n = 21

# se calcula el ancho de cada intervalo
h = (b - a)/(n - 1)

# Nota: para calcular la integral se va a definir el vector de pesos como 
# [1,4,2,4,2,...,1] de forma en que al sumar (f(a)+4f(a+h)+...+f(b)) solo
# se deba multiplicar por h/3

# se define el vector de pesos según lo explicado anteriormente
vectorPesos = []
for i in range(n):
    if i == 0 or i == n - 1:  #Cuidando que el for empieza a contar en 0
        vectorPesos.append(1)
    elif i % 2 != 0:
        vectorPesos.append(4)
    else:
        vectorPesos.append(2)
    
# se inicializa el valor de la sumatoria
suma = 0.0

# se realiza la sumatoria
for j in range(len(vectorPesos)):
    suma += vectorPesos[j]*F(a+j*h)
  
# se multiplica la suma anterior por h/3 para tener el resultado de la integral
resultadoIntegral = h/3*suma

# se muestra el resultado de la integral
print("El desplazamiento del automóvil en el intervalo indicado es x =",round(resultadoIntegral,1),"m")


# -----------------------------------------------------------
# Encontrar la raíz de una función mediante el método de
# Newton Raphson

# se define la función para la cual se va a calcular su 
# intersección con el eje x
def V(t):
    valorV = -5+1/2*0.01*t**2
    return valorV

# se establece el valor x con el que iniciar
t0 = 2;

# se define el ancho de intervalo h para calcular la derivada
h = 0.001

# se fija el nivel de tolerancia deseado
tol = 0.00001

# se define el número máximo de iteraciones para el método
iterMax = 10

# se inicializa el contador 
k = 1

# se inicia el ciclo
while k <= iterMax:
    
    # se calcular la derivada de la función por diferencias centradas
    derivadaV = (V(t0 + h) - V(t0 - h))/(2*h)
    
    # se calcula la intersección de la recta tangente con el eje x
    t1 = t0 - V(t0)/derivadaV
    
    if k > 1: # debe ser mayor a 1 porque si k = 0 todavía no 
              # se puede calcular el error
        error = abs(t1-t0)/t1
        if error < tol:
            break   
    
    # se actualiza el punto
    t0 = t1
    
    # Repetir con el nuevo punto hasta obtener la precisión deseada
    k += 1

# se muestra el resultado del cálculo  
print("Tiempo en el que el objeto pasaría por la posición x = 0.00 m: t = ",round(t1,1),"s")


