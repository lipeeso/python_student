
'''
Funções em Python - Parte 1 
'''
'''Para evitar de dar erro de posicional argumento basta declarar valores padrão dentro dos paramêtros para não dar erro'''


# def funcao(msg):
#     print(f'Olá, {msg}')
    
# def saudacao(msg, name):
#     print(msg, name)
    

# saudacao('Olá', 'Felipe')
    
# def soma(a,b):
#     print(a+b)
    


#funcao()



#soma(10,50)

# def funcao_teste(number):
    
#     if number == 1:
#         return 'Impar'
    
#     elif number == 2: 
#         return 'par'



# contador = 0 

# while contador <=10:
#     teste = funcao_teste(1)
    
#     if teste == 1:
#         break
#     elif teste == 2:
#         break
    
#     contador+=1 
    
# print(teste)
'''Tem como padronizar '''
def mensagem(msg='Olá', name='Felipe'):
    name = name.replace('e', 'i')
    msg = msg.replace('O', '0')
    print(msg, name)
    
mensagem()