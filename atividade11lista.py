#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

vector_age=[]
vector_height=[]

for i in range(5):
    age=int(input(f"Enter your age user {i + 1}:"))
    height=float(input(f"Enter your height user {i + 1} (in meters):"))

#Adicionando valores aos vetores
    vector_age.append(age)
    vector_height.append(height)

#Imprimindo as idades e alturas na ordem inversa:
print("\n Ages in reversed order:")
for age in reversed(vector_age):
    print(age)
print("\n Height in reversed order:")
for height in reversed(vector_height):
    print(height)



