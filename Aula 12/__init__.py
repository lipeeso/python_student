'''

QUANTIDADE DE CARACTER DENTRO DE UMA STRING PARA ISSO USAMOS A FUNÇÃO LEN

OBS: ELA NÃO FUNCIONA COM TIPOS NÚMERICOS
'''

'''usuario = input('Digite seu usuário: ')

qtd_caracteres = len(usuario)'''

#print(usuario, qtd_caracteres, type(qtd_caracteres))

'''if qtd_caracteres < 6:
    print('Você precisa pelo menos digitar 6 caracteres')
else:
    print('Você foi cadastrado no sistema)'''

#Somando a quantidade de caractere de 2 input do tipo string

string1 = input('Digite seu nome: ')
string2 = input('Digite seu nome: ')

print(f'A quantidade de string é {len(string1) + len(string2)}')

print(string2.__len__()) #outro jeito de ver o comprimento é chamar o metodo
