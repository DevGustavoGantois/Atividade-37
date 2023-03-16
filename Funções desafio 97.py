print("""Faça um programa que tenha uma função chamada escreva(), receba um texto qualquer como parâmetro e mostre
uma mensagem com tamanho adaptável.
Ex:
escreva(Olá Mundo!) Saída:
-------
Mundo
------- """)

def escreva(msg):
    tam = len(msg) + 4  
    print(tam * '-=')
    print(f'   {msg}')
    print(tam * '-=')


#Programa principal.
escreva('Gustavo Gantois')
escreva ('29/09/2003')
escreva('Gustavo tem 19 anos.')
