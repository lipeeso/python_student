'''Funções lambda'''


'''
Lambda é uma função anônima, ou seja, não possui nome.
Ela é definida usando a palavra-chave 'lambda' seguida de uma lista de parâmetros, dois pontos

'''

'''Função normal'''
def funct(args1, args2):
    return args1 * args2


var = funct(20, 30)

print(var)

'''Função lambda'''
'''
depois da palavra-chave 'lambda', você define os parâmetros e, em seguida, o corpo da função e retorna o resultado.
A função lambda é útil para criar funções pequenas e simples que são usadas apenas uma vez.
'''
a = lambda args1, args2: args1 * args2

print(a(20, 30))


'''Função lambda exemplo 2'''

lista = [
    ['p1',10],
    ['p2', 6],
    ['p3', 7],
    ['p4', 12],
    ['p5', 15]
]   

def func(item):
    return item[1]  # Retorna o segundo elemento de cada sublista

#lista.sort(key=lambda item: item[1])  # Ordena a lista com base no segundo elemento de cada sublista
print(sorted(lista, key=lambda item: item[1], reverse=True))  # Ordena a lista com base no segundo elemento de cada sublista

'''Se o reverse for True, a lista será ordenada em ordem decrescente. Se for False, será ordenada em ordem crescente.'''