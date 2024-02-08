#Crie um processador de texto simples que realiza várias operações
#em um texto de entrada, como contar palavras, contar letras,
#inverter o texto e substituir palavras-chave.
#Requisitos:
#Crie uma função chamada processador_texto que aceite uma
#string de texto como argumento.

#A função deve aceitar uma série de operações como argumentos
#de palavra-chave, usando **kwargs. As operações podem incluir
#"contar_palavras","contar_letras","inverter_texto"e"substituir_palavra".Use funções 
#lambda para realizar as operações de acordo com as palavras-chave especificadas nos 
#argumentos de palavra-chave.

#Se a operação"substituir_palavra " for especificada, a função deve aceitar uma 
#palavra-chave adicional, como "substituir_palavra"e" nova_palavra", para realizar a
#substituição em todo o texto.A função deve retornar o texto resultante após todas as
#operações.

def text_processor(text='My eggs', **kwargs):
    result_text = text

    if 'contar_palavras' in kwargs:
        contar_palavras = lambda x: len(x.split())
        result_text = contar_palavras(result_text)

    if 'contar_letras' in kwargs:
        contar_letras = lambda x: len(x.replace(' ', ''))
        result_text = contar_letras(result_text)

    if 'inverter_texto' in kwargs:
        inverter_texto = lambda x: x[::-1]
        result_text = inverter_texto(result_text)

    if 'substituir_palavra' in kwargs:
        palavra_a_substituir = kwargs.get('substituir_palavra', '')
        nova_palavra = kwargs.get('nova_palavra', '')
        substituir_palavra = lambda x: x.replace(palavra_a_substituir, nova_palavra)
        result_text = substituir_palavra(result_text)

    return result_text

# Exemplo de uso da função
texto_entrada = "Hello, my name is John. I like pizza."
resultado = text_processor(text=texto_entrada, contar_palavras=True, contar_letras=True, inverter_texto=True, substituir_palavra='John', nova_palavra='Jane')

print("Resultado:", resultado)
