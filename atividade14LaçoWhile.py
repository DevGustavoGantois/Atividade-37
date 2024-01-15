#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

anos=0

pais_A_populaçao=80000 #Taxa de crescimento de 3%
pais_B_populaçao=200000 #Taxa de crescimento de 1.5%

crescimento_do_pais_A=0.3
crescimento_do_pais_B=0.015

while pais_A_populaçao <= pais_B_populaçao:
    pais_A_populaçao *= crescimento_do_pais_A + 1
    pais_B_populaçao *= crescimento_do_pais_B + 1
    anos += 1

print(f"Serão necessários {anos} anos para que a popualçao do pais A ultrapasse a população do país B.")