valor = float((input('Qual é o preço do produto? R$')))
des = float(input('Qual é a porcentagem de desconto? '))
preço = valor - ((valor * des) / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de {:.0f}% vai curtar R${:.2f}.'
      .format(valor, des, preço))