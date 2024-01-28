#Crie dois conjuntos, A e B, e realize a união dos dois conjuntos.

set_A={'Gustavo', 'Yuri', 'Augusto', 'Nayra', 'Lucas', 'Rodrigo', 'Jorge'} 
set_B={'Guilherme', 'Cauã', 'Gabriel', 'Caique', 'Pedro', 'Paul', 'Matheus'}

#Usei o update para unir o dicionário A com o dicionário B e formar um só.
set_A.update(set_B)
print(set_A)
#imprimi o set_A unificado com o set_B.