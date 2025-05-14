"""
For/Else em Python

OBS: A FUNÇÃO STARTWITH CHECA SE O VALOR DA STRING COMEÇA COM UMA DETERMINADA LETRA


"""

# lista = [1, 2, 3, 4, 5]


# for n in lista:
#     print(n)
    
# contador = 0

# while contador < 10:
#     print(contador)
#     contador += 1   
lista = ['João', 'Rafael', 'Felipe']

# for n in lista:
#     if n.startswith('J'):
#         print('Começa com a letra J', n)
        
#     else:
#         print('Não começa com a letra J', n)

#comeca_w_j = False
for letra in lista:
    if letra.lower().startswith('j'):
        continue
        
    print(letra)
       
        
# if comeca_w_j:
#     print('Existe uma palavra que começa com J.')

# else: 
#     print('Não existe uma palavra que começa com J ')
    