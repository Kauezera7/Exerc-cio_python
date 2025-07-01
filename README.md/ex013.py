sal = float(input('Qual é o salário do funcionário? R$'))
aum = float(input('Qual é a porcentagem de aumento?'))
didi = sal + ((sal * aum) / 100)
print ('O funcionário que ganhava R${}, com {:.0f}% de aumento, passo a receber R${:.2f}.'.format(sal, aum, didi))
4