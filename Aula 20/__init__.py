'''
Iterando String com While

PARA COMENTAR AQUI NO PYCHARM USAR = CTRL + /

OBS: SE O ELEMENTO TEM INDICES ELE É ITERAVEL

UPPER É UMA FUNÇÃO DA STRING QUE CONVERTE A LETRA PARA MAIÚSCULA

LOWER É UMA FUNÇÃO DA STRING QUE CONVERTE A LETRA PARA MINÚSCULA

O SINAL += PARA STRING É CONCATENAÇÃO E PARA INTEIRO É SOMA

Iterar = Percorrer item por item dentro de algo (como uma lista, string, tupla, etc.)

OBS: O While é usado quando a gente itera sobre algo quando não sabemos o fim

'''

'''name = 'Felipe'
print(len(name))'''

# contador = 0
#
# while contador <= 10:
#     print(contador)
#
#     contador+= 1

'''AQUI ELE VAI ITERAR SOBRE A QUANTIDADE QUE EU COLOQUEI 14'''

# frase = 'Felipe Oliveira'
# contador = 0
#
# tamanho_texto = len(frase)
#
# while contador <= 14:
#     print(frase[contador], contador)
#     contador+= 1

'''AQUI ELE VAI ITERAR SOBRE O TAMANHO DA FRASE'''

# frase = 'O rato roeu a roupa do rei de roma'
#
# tamanho_text = len(frase)
#
# contador = 0
#
# while contador < tamanho_text:
#     print(frase[contador], contador)
#     contador+= 1

'''frase = 'Felipe'

tamanho_frase = len(frase)

contador = 0

while contador < tamanho_frase:
    print(frase[contador], contador)

    contador+= 1

print('Acabou o laço')'''

'''VAMOS PEGAR UMA STRING VAZIA E JOGAR A FRASE DENTRO DELA ATRAVÉS DO WHILE'''

'''frase = 'Felipe'

tamanho_frase = len(frase)

nova_string = ''

contador = 0

while contador < tamanho_frase:
    nova_string+= frase[contador] #ISSO É UMA CONCATENAÇÃO
    print(nova_string)
    contador += 1'''

'''AQUI EU VOU CRIAR UMA VALIDAÇÃO PARA PEGAR UMA LETRA MINUSCULA E COLOCAR MAIUSCULA'''
'''frase  = 'Felipe Olviveira'

tamanho_texto = len(frase)

nova_string = ''

contador = 0

while contador < tamanho_texto:
    letra = frase[contador]

    if letra == 'e':
        nova_string+= 'E'
    else:
        nova_string+= letra

    contador+= 1

print(nova_string)'''

'''frase = 'Felipe Oliveira'

tamanho_texto = len(frase)

nova_string = ''

input_letra = input('Digite uma letra que você quer deixar maiúscula: ')

contador = 0

while contador < tamanho_texto:
    letra = frase[contador] #AQUI ELE VAI ITERAR SOBRE A FRASE 

    if letra == input_letra:
        nova_string+= input_letra.upper() #AQUI EU VOU CONCATENAR A LETRA MAIUSCULA DENTRO DA NOVA STRING

    else:
        nova_string+= letra #AQUI EU VOU CONCATENAR (JUNTAR) A VARIAVEL NOVA_STTRING COM A VARIAVEL LETRA 

    contador+= 1

print(nova_string)
'''
'''
O WHILE VAI PASSAR LETRA POR LETRA DENTRO DO INDICE E VAI CAIR DENTRO DO IF E VAI CONCATENAR COM A LETRA QUE FOI DIGITADA DENTRO DO INPUT E VAI SE TORNAR MAIÚSCULA
'''
frase = 'felipe Oliveira'

tamanho_texto = len(frase)

input_letra = input('Digite uma letra: ')

nova_string = ''

contador = 0

while contador < tamanho_texto:
    letra = frase [contador]

    if letra == input_letra:
        nova_string += input_letra.upper()

    else:
        nova_string+= letra

    contador+= 1

print(nova_string)
