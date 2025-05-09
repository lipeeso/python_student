'''

Lista em Python
Fatiamento
append, insert, pop, del, clear, extend, + , min, max
Range

Faltou: clear, + e Range

'''

##################################--Lista--##########################################################
#OBS: uma variável só suporta um único valor, já uma lista suporta vários valores que podem ser de vários tipos diferentes
#-Uma lista é feita por colchetes -> []

#lista = ['FELIPE','BIA','CARLOS', 10.5, 1, 2, 3]
#-Para mudar o valor que está dentro de uma lista -> lista[2] = 'FP'
#print(lista[::-1])

##################################--Fatiamento--##########################################################
#-Para inverter a ordem da lista basta usar -> print(lista[::-1])
#print(lista[Começo:Fim:Step])

##################################--Função extend--##########################################################
#-A função extend serve para extender uma lista
#Por exemplo:
# l1 = [1,2,3]
# l2 = [4,5,6]
# l1.extend(l2)
# print(l1)

##################################--Função append--##########################################################
#-É usado quando a gente quer adicionar valores em uma lista
# l1 = [1,2,3]
#
# l1.append('A')
#
# print(l1[3])

##################################--Função insert--##########################################################
#-Com insert a gente pode inserir um valor na posição que a gente quiser dentro de uma lista

# l1 = [1,2,3,4,5,6]
#
# l1.insert(0, 'Felipe')
#
# print(l1)

##################################--Função pop--##########################################################
#-Com a função pop a gente consegue deletar o último elemento no final da lista

# l1 = [1,2,3,4,5]
# print(l1)
# l1.insert(0,'Felipe')
# print(l1)
# l1.pop()
# print(l1)

##################################--Função del--##########################################################
#-Para selecionar e excluir os indices basta chamar a função del() e passar como parâmetro um fatiamento do inicio ao fim

# l1 = [1,2,3,4,5,6,7,8,9]
# print(l1)
# del(l1[0:5])
# print(l1)

##################################--Função max e min--##########################################################
#-Para pegar o valor máximo da lista basta chamar a função max que retorna o maior valor da lista
# lista = [1,2,3,4,5,6,7,8,9]

# print(max(lista))

#-Para pegar o valor minimo da lista basta chamar a função min que retorna o menor valor da lista

# print(min(lista))

##################################--Função range--##########################################################
#-Listando usando a função range
# OBS: Podemos usar dentro da função range outra função chamada list que converte obj iteravél em uma lista

# list = list(range(0,101,5))
# print(list)

#Também podemos iterar sobre uma lista ex:
# list = [1,2,3,4,5,6,7,8,9,10]
#
# soma = 0
# for n in list:
#     soma = soma + n
#
# print(soma)

#iterando sobre uma lista com varios elementos
# list = ['String', True, 10, 10.5]
#
# for element in list:
#     print(f'O tipo desse elemento é {type(element)} e o valor é {element}')


