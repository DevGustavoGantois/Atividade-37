#Crie um programa que exiba os itens exclusivos de dois
#dicionários. Itens exclusivos são aqueles que não estão presentes em ambos os dicionários.

#Dois dicinários
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "c": 3, "d": 4}

#Obtém as chaves exclusivas de cada dicionário
keys_exclusives_dict1 = set(dict1.keys() - set(dict2.keys()))
keys_exclusives_dict2 = set(dict1.keys() - set(dict2.keys()))

#Obtém os itens exclusivos de cada dicionário com base nas chaves exclusivas
itens_exclusives_dict1 = {key: dict1[key] for key in keys_exclusives_dict1}
itens_exclusives_dict2 = {key: dict2[key] for key in keys_exclusives_dict2}

#Exibe os itens exlusivos de cada dicionário
print("Exclusive Items in first dictionary:", itens_exclusives_dict1)
print("Exclusive items in second dictionary:", itens_exclusives_dict2)
