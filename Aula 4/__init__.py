'''
Operadores Aritméticos

+ = Adição
- = Subtração
* = Multiplicação
/ = Divisão real
// = Divisão inteira
** = Exponenciação
%  = Módulo o resto da divisão entre um número e outro
() = Precedência
----------------------------------------------------------------

                    Concatenação

Não se concatena str com int

ex: print('teste' + 123) -> Isso está errado

ex: print('teste', 123 ) -> Jeito certo

Obs: Você tem a opção de usar type casting para converter o int por str

ex: print('teste' + str(123))

-------------------------------------------------------------------
                        Ordem de Precedência

Ordem de precedência siginifica quem vai ser executado primeiro:

1 - Parentese que fica dentro de uma função ( )

2 - Potência **

3 -  Multiplicação, Divisão, Divisão inteira, Resto da divisão

4 - Soma e Subtração
'''

number = 123

print('teste', number)

print('teste' + str(123))

print(type(number))

