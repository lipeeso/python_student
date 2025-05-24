"""
Operador ternário

"""

logged_user = True

'''Utilizando operador ternário'''

idade = input('Digite sua idade: ')

if not idade.isnumeric():
    print('Você precisa digitar somente números.')
else:
    idade = int(idade)
    idade_maior = (idade>=18)
    msg = 'Pode acessar' if idade_maior else 'Não pode acessar'
    print(msg)

# msg = 'Usuário logado' if logged_user else 'Usuário precisa logar'
# print(msg)

"""Jeito tradicional"""
# if logged_user: #Isso é identico a isso daqui -> if logged_user == True
#     msg = 'Usuário logado.'
# else:
#     msg = 'Usuário precisa logar.'

# idade = 18
#
# if idade >= 18:
#     print('Pode acessar')
# else:
#     print('Não pode acessar')
