dis = float(input('Qual a distância da viagem? '))
if dis <= 200:
    preco = dis * 0.50
else:
    preco = dis * 0.45
print(f'O preço da sua passagem é de R${preco:.2f}.')
