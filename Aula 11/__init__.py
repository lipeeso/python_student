'''
OPERADOS LÓGICOS:

and, or, not, in e not in

and: Retorna True se ambas as condições forem verdadeiras.

    Exemplo: True and False → False
    Exemplo: True and True → True

or: Retorna True se pelo menos uma condição for verdadeira.

    Exemplo: True or False → True
    Exemplo: False or False → False

not: Inverte o valor lógico de uma condição. Se for True, retorna False, e se for False, retorna True.

    Exemplo: not True → False
    Exemplo: not False → True

in: Verifica se um valor está dentro de uma sequência (como lista, tupla ou string). Retorna True se o valor estiver presente.

    Exemplo: 'a' in 'banana' → True
    Exemplo: 3 in [1, 2, 3] → True

not in: Verifica se um valor não está dentro de uma sequência. Retorna True se o valor não estiver presente.

    Exemplo: 'z' not in 'banana' → True
    Exemplo: 4 not in [1, 2, 3] → True

'''


'''
Exemplo do 'and'

a = 10
b = 10
c = 9

if a == b and b > c:
    print('True')

else:
    print('False')

'''

'''Exemplo do or

a = 10
b = 10
c = 9

if a == b or b < c:
    print('True')

else:
    print('False')
'''

'''Exemplo do not

OBS: O not ele inverte o valor

a = 10
b = 5

if not b > a:
    print('A é maior que B')
else:
    print('B é maior que A')

'''

'''
Exemplo do in

name = 'Felipe'

if 'F' in name:
    print('Existe a letra F no seu nome')
else:
    print('Não existe essa letra no seu nome')

'''

'''

Exemplo not in

 name = 'Felipe'

if 'asdf' not in name:
    print('Não existe essa letra no seu nome')
else:
    print('Existe')
 
'''


'''
Exercicio de validação de usuário


user_name = input('Digite seu usuário')
password_user = int(input('Digite sua senha'))

user_db = 'Felipe123'
password = 12345

if user_name == user_db and password_user == password:
    print('Login feito com sucesso')

else:
    print('Login ou senha incorreto')

'''
















