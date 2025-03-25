'''

Tipos de dados

str - String = Tipo de texto ex : "texto" 'texto'
int - Inteiro = São números ex: 12345 -1-2-3-4-5
float - Real/Ponto Flutuante  = São números quebrados ex: 1,0, 0,2
bool - Booleano/Lógico = True ou False 10 == 10

UMA LISTA VAZIA SEMPRE SERÁ FALSE
Lista vazia = [] False
Aspas vazia = "" False
Colchetes vazio = () False

'''

'''Para ver o tipo primitivo usar type()'''

print('Felipe', type('Felipe'))
print(10, type(10))
print(10.1, type(10.1))
print(10 == 10, type(10 == 10)) #Sinal de comparação "=="

#----------------------------------------------------------------------------------------------------#
'''
Type casting: 
Converte um tipo para outro 

'''

print('Felipe', type('Felipe'), bool('Felipe'))

print('100',type("100"), type(int('100')))

print('felipe', type(bool('felipe')))


'''-------------------------------------------------------------------------------------------------------'''
#Exercicios:

#String: Nome
print('Felipe', type('Felipe'))
#Int: Idade
print(20, type(20))
#Float: Altura
print(1.66, type(1.66))
#Verificar se é de maior
print(20>18, type(20>18))