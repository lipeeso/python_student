'''
While / Else

Contadores e Acumuladores

'''

'''x = 50
while x <= 100: #ISSO AQUI É UM CONTADOR 
    print(x)
    x+= 1'''

'''
AQUI O ACUMULADOR VAI SER SOMADO COM O CONTADOR 

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador

    contador+= 1
'''

''' ELSE SÓ SERÁ EXECUTADO QUANDO A EXPRESSÃO FOR FALSE, E SE O LAÇO FOR QUEBRADO O ELSE NÃO SERÁ EXECUTADO'''
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador == 5:
        break

    acumulador = acumulador + contador

    contador+= 1
else:
    print('Cheguei aqui')
