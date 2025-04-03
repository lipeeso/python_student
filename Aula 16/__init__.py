'''
Formatando valores com modificadores - Aula 5

:s - Texto (Strings)
:d - Inteiros (int)
:f - Float (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
: (CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda 

< - Direita

^ - Centro	

# -> Se chama cerquilha 

'''

# num_1 = 10

# num_2 = 3 

# divisao = num_1 / num_2

# print('{:.2f}'.format(divisao))


# nome = 'Felipe Oliveira'

# print(f'{nome:s}')

num_1 = 1

print(f'{num_1:0>10}') 

num_2 = 1150

print(f'{num_2:0>10}')

num_3 = 12345

print(f'{num_3:0^10}')