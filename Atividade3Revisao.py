#Crie um conjunto com nomes de cores. Implemente uma
#função que retorne as cores que têm mais de quatro
#letras.

colors = {'Yellow', 'Red', 'Green', 'Blue', 'Magenta', 'Purple'}


def collors_four_letters():
       result = {color for color in colors if len(color) > 4}
       return result

result_collors_four = collors_four_letters()
print(result_collors_four)