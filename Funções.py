def soma (a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de {a} + {b} = {s}')
    print(s)

#Programa principal
soma(a=4, b=5)
soma(a=8, b=9)
soma(a=2, b=1)

def contador(*num):
    tam = (f'Recebi os valores de {num} é são ao todo {tam} números')





def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 1, 0, 9, 2]
dobra(valores)
print(valores)



def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)


