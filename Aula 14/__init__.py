'''
pass: É uma instrução que não faz nada. Usado quando você precisa de uma estrutura (como uma função ou condição) que ainda não tem implementação.

ellipsis (...): Representado por três pontos, é um marcador de lugar. Pode ser usado para indicar que algo será implementado futuramente ou, em bibliotecas como o NumPy, como atalho para trabalhar com arrays multidimensionais.
'''

def teste():
    valor = False

    if valor:
        pass

    else:
        print('Tchau')


teste()