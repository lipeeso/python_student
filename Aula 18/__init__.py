'''
While - Estrutua de repetição em Python

Utilização para realizar ações enquanto uma condiçãoo for verdadeira

Requisitos: Entender condições e operadores

Sempre que ele achar um 'continue' ele vai pular para o próximo laço

A palavra 'break' finaliza o loop

Para incrementar pode utilizar duas maneiras x = x +1 ou x+=1

'''


'''while True: #Loop infinito
    name = input('Digite seu nome: ')
    print(f'Olá {name}')

print('Esse bloco não será executado')'''

'''x = 0
while x < 5:
    print(x)
    x = x +1

print('Acabou!')'''

'''
x = 0
while x < 10:
    if x == 5:
        x = x + 1
        continue

    print(x)
    x = x+1
print('Acabou!')
'''

'''x = 0

while x < 10:
    if x == 3:
        x = x + 1
        break

    print(x)
    x = x+1 
print('Acabou!')
'''

"""
x = 0
while x < 10:
    y = 0
    while y < 5:
        print(f' ({x},{y})')
        y+= 1

    x+=1 # isso é a mesma coisa que x = x + 1
print('Acabou!')

"""

'''
A cada 4 voltas dentro do y ele conta 1 volta dentro do x
'''

'''
Fazendo uma calculadora dentro de um while True
'''

'''
while True:
    print() # esse print serve para pular um linha no terminal
    num_1 = input('Digite um número: ')
    num_2 = input('Digite um outro número: ')
    operador = input('Digite um operador: ')

    #sair = input('Deseja sair? [S]im ou [N]ão ?')


    if not num_1.isnumeric() or not num_2:
        print('Você precisa digitar um número')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)

    elif operador == '-':
        print(num_1 - num_2)

    elif operador == '/':
        print(num_1 / num_2)

    elif operador == '*':
        print(num_1 * num_2)

    else:
        print('Operador inválido')

    sair = input('Deseja sair? [S]im ou [N]ão ?')

    if sair == 'S':
        break'''

'''
x = 0
while x < 10:
    if x == 5:
        x = x + 1
        continue

    print(x)
    x = x+1
print('Acabou!')

'''

x = 0
while x < 10:
    if x == 5:
        break

    print(x)
    x+= 1

print('Acabou')

