import random
n1 = input('Digite o primeiro nome:')
n2 = input('Digite o segundo nome:')
n3 = input('Digite o terceiro nome:')
n4 = input('Digite o quarto nome:')
nome = [n1,n2,n3,n4]
#sorteio = random.shuffle(nome)
random.shuffle(nome)
#random.sample(dá para ser ultilizado)
print('Ordem dos sorteados:')
print(nome)