'''Funções com *args e **kwargs '''




'''Esses args estão empacotados em uma tupla e em tuplas o valor não podem ser alterados'''
def func(*args, **kwargs):
    args = list(args) #typecasting
    args[0] = 10 
    print(args)
    print(args[0]) #acessando o primeiro valor 
    print(args[-1]) #acessando o ultimo valor 
    print(len(args)) #Para saber quantos argumentos eu tenho no args 




'''For em args'''
def func_args(*args, **kwargs):
    for index in args:
        print(index)




'''Lista '''


def func_list(*args):
    print(args)


lista = [1,2,3,4,5]
'''se não desempacotar essa lista dentro de args vai aparecer uma lista dentro de uma tupla'''
#print(func_list(lista)) 
#print(func_list(*lista,1))

'''Função usando *args e **kwargs= argumentos com palavras chaves'''
'''OBS: Quando for acessar uma chave em **kwargs usar sempre o .get para procurar o valor da chave se não o script vai quebrar'''
  
def function(*args, **kwargs):
    print(args)
    #print(kwargs['name'], kwargs['age'])
    name = kwargs.get('name')
    age = kwargs.get('age')
    high = kwargs.get('high')
    
    if age is not None:
        print(age)
    else:
        print('Age not found')

    if name is not None:
        print(name)
    else:
        print('Name not found')

    if high is not None:
        print(high)
    else:
        print('Name not found')

print(function('Seu nome:', name='Felipe', age=23))

'''*args é uma tupla e **kwargs é um dict'''


'''Tira isso como exemplos para ter uma ideia de *args e **kwargs'''
# lista = [1,2,3,4,5]

# n1, n2, *_ = lista

'''Aqui eu to desempacotando a lista'''
# print(*lista, sep='-') 