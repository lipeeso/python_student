"""
For in em Python
Iterando String com for
Função range(Start=0, stop step=1)
O Laço for é utilizado para coisas infinitas
"""
from distutils.msvccompiler import normalize_and_reduce_paths

#Para iterar sobre o text
text = 'Python'

'''for letra in text:
    print(letra)'''

#Para iterar com o contador basta implementar a função enumerate

'''for i,letra in enumerate(text):
    print(i, letra)'''

#Usando a função range dentro do for

'''for n in range(10):
    print(n)'''

#Usando a função range contando do maior para o menor
#OBS: Para contar do maior para o menor basta colocar no parametro 'step' o número -1
'''for n in range(20,10,-1):
    print(n)'''

#Passando uma frase para um nova string

frase = 'Python'
nova_string = ''

'''for letra in frase:
    if letra == 'y':
        nova_string+= letra.upper()
    elif letra == 'h':
        nova_string+= letra.upper()
    else:
        nova_string+= letra

print(nova_string)'''

for letra in frase:
    nova_string+= letra

print(nova_string)