#!/usr/bin/env python
# coding: utf-8

# #ejercicio 1
# print ("Hola Mundo")

# In[ ]:


#ejercicio 2

nombre = input("Ingresa tu nombre")
print(f"Hola {nombre}!")


# In[ ]:


#ejercicio 3

nombre = input("Ingresa tu nombre")
apellido = input("Ingresa tu apellido")
edad= input("Ingresa tu edad")
lugar = input("ingresa tu lugar de residencia")
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")


# In[ ]:


#ejercicio 4

import math

radio = float(input("Ingresa el radio del circulo"))
area = math.pi * (radio)**2
perimetro = 2 * math.pi * radio

print (f"el area del circulo es {area} y el perimetro es {perimetro}")


# In[ ]:


#ejercicio 5

import math


segundos = float(input("ingresa la cantidad de segundos"))
horas= round(cantidad_segundos/3600 , 2)
print(f"{segundos} segundos equivalen a {horas} horas")


# In[ ]:


#ejercicio 6


num = int(input("Ingrese su numero"))

print(f"Tabla de multiplicar del {num}:")

numero_por_0 = num* 0
numero_por_1 = num* 1
numero_por_2 = num * 2
numero_por_3 = num * 3
numero_por_4 = num * 4
numero_por_5 = num * 5
numero_por_6 = num * 6
numero_por_7 = num * 7
numero_por_8 = num * 8
numero_por_9 = num * 9


print(f"""
    {num} x 0 = {numero_por_0}
    {num} x 1 = {numero_por_1}
    {num} x 2 = {numero_por_2}
    {num} x 3 = {numero_por_3}
    {num} x 4 = {numero_por_4}
    {num} x 5 = {numero_por_5}
    {num} x 6 = {numero_por_6}
    {num} x 7 = {numero_por_7}
    {num} x 8 = {numero_por_8}
    {num} x 9 = {numero_por_9}
        """)


# In[ ]:


#Ejercicio 7

num1 = int(input("Ingresá el primer número(distinto de 0): "))
num2 = int(input("Ingresá el segundo número (distinto de 0): "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


# In[ ]:


#ejercicio 8

altura = float(input("Ingresá tu altura en metros: "))
peso = float(input("Ingresá tu peso en kilogramos: "))

imc = peso /(altura ** 2,2) 
print(f"Tu índice de masa corporal es: {imc:}")


# In[ ]:


#ejercicio 9

celsius = float(input("Ingresá la temperatura en grados Celsius: "))
fahrenheit = round((9/5)*celsius+32,2)
print(f"{celsius}°C equivalen a {fahrenheit}°F")


# In[ ]:


#ejercicio 10

num1 = float(input("Ingresá el primer número: "))
num2 = float(input("Ingresá el segundo número: "))
num3 = float(input("Ingresá el tercer número: "))

suma = num1 + num2 +  num3

promedio = round(suma/3, 2)

# Mostrar resultado
print(f"El promedio de los números es: {promedio}")


# In[ ]:




