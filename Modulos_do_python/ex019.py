import random
pri = input('Digite o primeiro nome:')
seg = input('Digite o segundo nome:')
ter = input('Digite o terceiro nome:')
qua = input('Digite o quarto nome:')
nome = [pri, seg, ter, qua]
sor = random.choice(nome)
print(f'Nome sorteado:{sor}')