#Desenvolva um programa que permita ao usuário
#converter entre diferentes unidades de medida, como
#metros para pés, quilogramas para libras, ou Celsius
#para Fahrenheit. Use módulos que contenham funções
#de conversão.

import ConverterUnidadeDeMedida


kg = float(input("Enter your weight: "))
print("<=======================================================================>")
result_kg_for_lbs = ConverterUnidadeDeMedida.kg_for_lbs(kg)
print(f"The weight in kg is {kg:.2f}kg and in lbs = {result_kg_for_lbs}lbs.")
print("<======================================================================>")
metters = float(input("Enter the height in metters:"))
result_metters_for_feet = ConverterUnidadeDeMedida.m_for_feet(metters)
print(f"The height in metters is {metters} and in feet = {result_metters_for_feet}")
celsius = float(input("Enter the temperature in Celsius:"))
result_celsius_fahrenheit = ConverterUnidadeDeMedida.celsius_fahrenheit(celsius)
print(f"The temperature in Celsius is {celsius} and in fahrenheit = {result_celsius_fahrenheit} ")
