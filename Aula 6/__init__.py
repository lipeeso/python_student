nome = 'Felipe'
idade = 22
altura = 1.65
e_maior = idade > 18
peso = 65
imc = peso / (altura ** 2)

print(nome,'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc}')
print('{} tem {} anos de idade e seu imc é {}'.format(nome,idade, imc ))


