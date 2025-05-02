'''
Manipulando String - Aula 6

* String indice

* Fatiamento de String [Inicio:fim:passo]

* Funções built-in len, abs, type, print etc...

Essas funções podem ser usadas diretamente em cada tipo.

'''

#Indices Positivos[0,1,2,3,4,5]
'''nome =         'F e l i p e'

print( nome[3] )'''

#Indices Negativos [-5,-4,-3,-2,-1,0]
'''name =           'F  e  l  i  p e'

print(name[:6])'''

#Fatiamento de uma string
# OBS: SE FOR PEGAR DO INICIO NÃO PRCISA INCLUIR O INDICE ELE PEGA O ZERO POR PADRÃO, ENTÃO FICARIA ASSIM [:5] E VICE E VERSA [0:]
#PARA PULAR CASA É NECESSARIO USAR: [0:6:2] AQUI ELE VAI PULAR 2 CASAS DO INDICE 0 ATÉ 0 6

texto = 'tecnologia'

#nova_string = texto[:]

print(texto.__len__()) #Para ver quantos caractere tem dentro de uma string usar a função built - in do Python