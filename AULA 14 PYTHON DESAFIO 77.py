print('===============================ATIVIDADE============================================================')
print("""Crie um programa que tenha uma Tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.""")
print('=='*40)
palavras = ('Corno', 'Viado', 'Fluido', 'Jose', 'NaoBinario', 'Todes', 'Misogeno', 'Stella')
for vogais in palavras:
    print(f'\nNa palavra {vogais.upper()} temos ', end= '')
    for letra in vogais:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

print('PROGRAMA ENCERRADO.')