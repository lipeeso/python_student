'''
Iniciar com letra, pode ter números, separar _, letras minúsculas

OBS: Variaveis não podem ser iniciadas com números

A FORMA MAIS RECOMENDADA PARA COCATENAR É UTILIZANDO O  F STRING
'''

'''nome = 'Felipe'
print(nome, type(nome)) #Type é para exibir o tipo da variavel

nome = 'Felipe'
idade = 22
altura = 1.65
e_maior = idade > 18

print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('De maior: ', e_maior)'''
'''
nome = 'Felipe'
sobrenome = 'Oliveira'
idade = 22

print(f'{nome} {sobrenome} {idade}')
'''

number_int = 22

number_float = float(number_int)
print(number_float, type(number_float))

print(type(float(12)))

print(float(42))


print('Felipe tem', 22)

nome = 'Felipe'

print('Olá meu nome é {}'.format(nome))

number_str = '12'

number_float = float(number_str)

print(number_float, type(number_float))

mes = 12

mes_str = str(mes)

print(mes_str, type(mes_str))

print(type(bool(12)))

nome = 'Felipe'
idade = 22
altura = 1.65
e_maior = idade > 18
peso = 65
imc = peso / (altura ** 2)

print(nome,'tem', idade, 'anos de idade e seu imc é', imc)

