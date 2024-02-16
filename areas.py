#Crie um programa que permite ao usuário calcular a
#área e operímetro de formas geométricas simples,
#como quadrados, retângulos e círculos. Use funções
#matemáticas do módulo math para realizar os cálculos.

#importando a biblioteca math para realizar os calculos
import math

def area_square(square):
    #Método pow faz que o valor seja elevado a o número solicitado.
    side_square = math.pow(square, 2)
    return side_square

square = int(input("Enter a side square:"))

def area_rectangle(b,h):
    rectangle = b*h
    return rectangle

b = int(input("Enter a base of rectangle:")) 
h = int(input("Enter a height of rectangle:"))

def area_circle(r):
    #math.pi mostra o valor de pi = 3.14
    circle = math.pi * math.pow(r,2)
    return circle

r = float(input("Enter a the value of circle radius:"))

#valor da area do quadrado:
result_square = area_square(square)
print('Area of square:',result_square)

#valor da area do retangulo:
result_rectangle = area_rectangle(b,h)
print('Area of rectangle:',result_rectangle)

#valor da area do círculo:
result_circle = area_circle(r)
print('Area of circle:',result_circle)