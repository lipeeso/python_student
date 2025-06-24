from random import randint #Gera número aleatório
'''
1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome
'''

# def saudacao(saudacao, nome):
#     return(f'{saudacao},{nome}')



'''
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles 

'''
# def sum(a, b, c):
#     return a + b + c

# return(sum(20, 50, 100))


'''
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado do aumento do
percentual do mesmo
'''
# def porcentage(value, porcentage):
#     return(value + (value * porcentage / 100)) 

# print(porcentage(100, 10))

'''
4 - Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da função
for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado. 

'''
def fb(n):
    '''
    Aqui ele não vai precisar de um elif por conta de que se cair na condição tem um return e nnão vai precisar checar outras condições 
    
    '''
    if n % 3 == 0 and n % 5 == 0:
        return f'FizzBuzz, {n} é divisivel por 3 e 5'
    if n % 2 == 0:
        return f'fizz, {n} é divisivel por 2'
    if n % 5 == 0:
        return f'buzz, {n} é divisivel por 5'
    
    return n
    

for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))

