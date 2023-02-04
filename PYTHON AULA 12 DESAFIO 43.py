print('                                         ATIVIDADE                                                ')
print('------------------------------------------------------------------------------------------------------')
print('Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Coporal (IMC) e ')
print('mostre seu status, de acordo com a tabela abaixo:')

print('-IMC abaixo de 18.5: Abaixo do peso. ')

print('-Entre 18.5 e 25: Peso Ideal.')

print('-25 até 30: Sobrepeso. ')

print('-30 até 40: Obesidade.')

print('Acima de 40: Obesidade Mórbida. ')
print('--------------------------------------------------------------------------------------------------------------')
peso = float(input('Qual o seu peso em kg?'))
altura = float(input('Qual a sua altura em M?'))
IMC = peso/altura**2
if IMC < 18.5:
        print('Você está com o seu IMC baixo {:.2f} e está abaixo do peso o seu peso é {} e seu altura é {} . '.format(IMC,peso, altura))
elif IMC == 18.5 or IMC <= 25:
        print('Você está com seu IMC adequado {:.2f}, com o peso ideal. O seu peso é {} e a sua altura é {} . '.format(IMC,peso, altura))
elif IMC == 25 or IMC <= 30:
    print('Você está com seu IMC um pouco elevado {:.2f}, está com sobrepeso. O seu peso é {} e a sua altura é {} . '.format(IMC, peso,altura))
elif IMC == 30 or IMC <= 40:
        print('Você está com seu IMC elevado {:.2f}, está com Obesidade. O seu peso é {} e a sua altura é {} . '.format(IMC, peso, altura))
elif IMC > 40:
        print('Você está com seu IMC muito elevado {:.2f}, está com Obesidade Mórbida. O seu peso é {} e a sua altura é {} . '.format(IMC,peso, altura))
