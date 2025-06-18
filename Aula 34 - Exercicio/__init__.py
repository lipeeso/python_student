'''
1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome
'''

def saudacao(saudacao, nome):
    print(f'{saudacao},{nome}')

saudacao('Olá', 'Felipe')


'''
2 - Crie uma função que recebe 2 números como parâmetros e exiba a soma entre eles 

'''
def sum(a, b):
    return a + b 

print(sum(20, 50))


'''
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado do aumento do
percentual do mesmo
'''
def porcentage(value, porcentage):
    return (value) + value / porcentage 

print(porcentage(50, 0.10))

'''
4 - Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da função
for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado. 

'''