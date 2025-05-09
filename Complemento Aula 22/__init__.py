'''
Criando o jogo da forca

'''

# secreto = 'Perfume'
# digitados = []
# chances = 3
#
# while True:
#     if chances <= 0:
#         print('Você perdeu')
#         break
#
#     letra = input('Digite uma letra')
#
#     #AQUI ELE VERIFICA SE DIGITOU MAIS DE UMA LETRA
#     if len(letra) > 1:
#         print('Isso não vale, digite apenas uma letra')
#         continue
#
#     #AQUI ELE VAI ADICIONAR A LETRA DENTRO DA LISTA
#     digitados.append(letra)
#
#     #AQUI ELE VAI VERIFICAR SE A LETRA EXISTE
#     if letra in secreto:
#         print(f'Essa letra {letra} existe na palavra secreta')
#     else:
#         print(f'Essa letra {letra} não existe na palavra secreta')
#         digitados.pop()
#
#     #AQUI ELE VAI PEGAR O QUE TEM EM SECRETO VAI PASSAR PARA VARIAVEL VAZIA (secreto_temporario) E VAI COMPARAR NO FINAL
#     secreto_temporario = ''
#     for letra_secreta in secreto:
#         if letra_secreta in digitados:
#             secreto_temporario+= letra_secreta
#         else:
#             secreto_temporario+= '*'
#
#     if secreto_temporario == secreto:
#         print(f'Você ganhou o jogo!! A palavra é {secreto_temporario}')
#
#     else:
#         print(f'A palavra secreto está assim: {secreto_temporario}')
#
#     #SE A LETRA NÃO TIVER EM SECRETO É MENOS UMA CHANCE
#     if letra not in secreto:
#         chances-= 1
#
#     print(f'Você ainda tem {chances} chances')
#     print()


###################################################################################################################################################
'''
jogo da forca 
'''
palavra = 'flamengo'
digitado = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu as 3 tentativas')
        break

    letra = input('Digite uma letra')

    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue

    digitado.append(letra)

    if letra in palavra:
        print(f'Essa letra {letra} existe na palavra secreta')

    else:
        print(f'Essa letra {letra} não existe na palavra secreta')
        digitado.pop()

    palavra_secreta = ''
    for letra_secreta in palavra:
        if letra_secreta in digitado:
            palavra_secreta+= letra_secreta
        else:
            palavra_secreta+= '*'

    if palavra_secreta == palavra:
        print(f'Parábens!! A palavra secreta é {palavra_secreta}')
    else:
        print(f'A palavra secreta está assim: {palavra_secreta}')

    if letra not in palavra:
        chances-= 1

    print(f'Você ainda tem {chances}')
    print()







