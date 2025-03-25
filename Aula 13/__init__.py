'''
Documentação e funções built-in úteis

Obs: Python é uma linguagem de tipagem dinamica assim como: Javascript e PHP

A função isnumeric valida se tem número inteiro dentro da string e lembrando que ela só entrega números inteiros apenas

Se converter o input logo de cara não vai ser possivel fazer a checagem do erro

OBS: Evitar Erros e Exceções: Quando você valida os dados ou as entradas antes de fazer algo com eles, você garante que o programa não falhará devido a dados incorretos. Se você tenta usar dados inválidos diretamente em operações, isso pode gerar exceções ou erros difíceis de tratar posteriormente. A validação antecipada evita isso.


'''

num1 = input('Digite um número: ')

num2 = input('Digte um número: ')

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)

else:
    print('Não foi possivel converter o número')

