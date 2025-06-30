din = float(input('Quanto dinheiro você tem na carteira? R$'))
cot = din / 5.46
print('Com R${:.2f} você pode comprar US${:.2f}'.format(din,cot))