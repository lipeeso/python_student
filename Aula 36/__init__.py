'''Funções part 4 - Escopo de variaveis '''

'''Escopo Global ela está acessivel em todo lugar do código'''

var = 'valor'

def func():
    print(var)

def func2():
    '''Escopo Local ela só está acessivel dentro da função'''
    '''Para alterar uma variável global dentro de uma função, é necessário declarar a variável como global dentro da função, mas não considerado uma boa prática'''
    #global var  # Declara que a variável 'var' é global
    var = 'Outro valor'
    print(var)

'''Outra forma de alterar uma variavel dentro da função '''
def func3(args=None):
    args = args.replace('v', 'c')

    return args





print(func3(var))
func()
func2()

print(var)  # Acessando a variável global

'''OBS: Alterar uma variavel de dentro de uma função não é considerado uma boa prática 

OBS: Não trabalhar com variáveis globais dentro de funções é uma boa prática, pois pode levar a código difícil de entender e manter.


'''
