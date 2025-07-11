'''Tuplas em Python'''

'''
Diferença de tupla para lista é que você não consegue editar os elementos da tupla

Você não pode remover e nem mudar o valor do indice

'''

'''Declarando uma tupla'''
tupla = (1, 2, 3, 4, 5, 'Felipe')

print(tupla[3])


'''É possivel declarar uma tupla sem parentese'''

tupla_sem_parentese = 1, 2, 3, 4, 5

print(type(tupla_sem_parentese))

'''Para declarar um elemento dentro de uma tupla basta colocar uma ',' no final mesmo se for declarar sem parentese '''

tupla_um_elemento = 1,

print(type(tupla_um_elemento))


'''Iterando um tupla'''
for elemento in tupla:
    print(elemento)

'''Também é possivel concatenar tuplas'''

t1 = (1, 2, 3, 4, 5)
t2 = ('a', 'b', 'c', 'd')
t3 = t1 + t2
print(t3)

'''Também é possivel desempacotar '''

n1, n2, n3, *_ = t3

print(n1, n2, n3)

'''Também é possivel multiplicar uma tupla '''

multiplicar = (1, 2, 3, 4, 5) * 20

print(multiplicar)

'''Podemos converter uma tupla em lista '''

tupla_normal = (1, 2, 3, 4, 5)
tupla_convertida = list(tupla_normal)
print(type(tupla_normal))
print(type(tupla_convertida))