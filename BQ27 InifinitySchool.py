idade=[]
peso=[]
altura=[]
quantidade = 0
q2=0

for x in range (0,10):
    idades= int(input(f"Digite sua idade {x} pessoa : "))
    pesos= float(input(f"Digite seu peso {x} em kg: "))
    alturas= float(input(f"Digitte sua altura {x} em metros: "))
    
    idade.append(idades)
    peso.append(pesos)
    altura.append(alturas)


media = sum(idade)/len(idade)
    
print (f"media das pessoas Ã© {media}")

for x in range(0,10):
     if peso[x] > 90 and altura[x] < 1.50:
        quantidade =+ 1
        print(f"{quantidade} pessoas!")
        
for x in range (0,10):
    
        
    if idade[x] > 10 and idade[x] <= 30 and altura[x] > 1.90:
        q2 =+ 1
        
        porcentagem = q2 / len([altura>1.90])*100
        
        print(f"{porcentagem} acima de 1,90 e tem idade de 10 a 30 anos!")
