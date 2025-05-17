"""
Split, Join e Enumerate em Python

* Split - Dividir uma string gerando uma lista

* Join - Juntar uma lista # str

* Enumerate - Enumerar elementos da lista # Iteraveis ele mostra o indices
"""


# string = 'O Brasil é o o país do futebol,  sim ou não?,  em?'

# lista = string.split(' ')  # Divide a string em uma lista 

# lista_2 = string.split(',')

#print('Está dentro da lista', lista)

# for valor in lista:
#     print(f'A palavra {valor} apareceu {lista.count(valor)}x na lista') #count() é usado para contar quantas vezes um determinado valor aparece em uma lista, tupla, ou em uma string.
    
# palavra = ' '
# contagem = 0

# for valor in lista:
#     qtd_vzs = lista.count(valor)
    
#     if qtd_vzs > contagem:
#         contagem = qtd_vzs
#         palavra = valor

# print (f'A palavra que apareceu mais vezes é {palavra} {contagem}x vezes')

# for valor in lista_2:
#     print(valor.strip().capitalize()) #strip remove o espaço entre o inicio e o fim
    
    
    
#########################################################################################################



# string = 'O brasil é penta campeão'

# lista = string.split(' ')

# string2 = ' '.join(lista)

# print(string)
# print(lista)
# print(string2)

lista = ['Felipe', 'Rafael', 'João', 'Matheus']

lista_junta = ' '.join(lista)

print(lista)
print(lista_junta)

###########################################################################################################

# string = 'Brasil é penta campeão'

# lista = string.split()

# print(lista)

# for indices, valor in enumerate(lista):
#     print(indices, valor)
    

# lista = [
#     ['Felipe'],
#     ['Maria'],
#     ['Camila']
# ]

# #print(lista)

# for i, name in enumerate(lista):
#     print(i, name)


##############################################################################################################


'''Desenpacotamento'''

# lista = [1,2,3]

# n1, n2, n3 = lista

# print(n2)