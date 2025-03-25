'''
------------------CONDIÇÕES IF, ELSE E ELIF -------------------

if = se

else = se não

elif = se não se

-----------------------------------------------------------------

Ordem = if , elif e else

if False:
    print('Verdadeiro')
elif False:
    print('AGORA É VERDADEIRO')
elif True:
    print('ESSA REALMENTE É VERDADEIRA')
else:
    print('NENHUMA É VERDADEIRO')

'''

'''name = input('Digite um nome: ')'''

'''if name == 'Rafael':
    print('Nome não aceito')
elif name == 'João':
    print('Nome não aceito')
elif name == 'Felipe':
    print(f'Nome: {name} validado com sucesso')'''

'''if name != 'Felipe':
    print('Recusado')
else:
    print('Nome aceito')'''

'''if name == 'Felipe' or name == 'João':
    print('Nome aceito')
else:
    print('Recusado')'''


login = input('Digite o login: ')

senha = int(input('Digite a senha: '))

if login == 'Felipe123' and senha == 123456 :
    print('Acesso correto')
else:
    print('Acesso negado')