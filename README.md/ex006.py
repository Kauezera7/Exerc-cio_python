num = int(input('Digite um número:'))
s = num * 2
t = num * 3 
r = num ** (1/2)
print('triplo de {} vale {}.'.format(num,t))
print('O dobro de {} vale {}.5\nA Raiz quadrada de {} é igual a {:.3f}'.format(num,s,num,r))

#ESSE É OUTRO MODO DE FAZER A EQUAÇÃO
print('triplo de {} vale {}.'.format(num,(t* 1)))
print('O dobro de {} vale {}.\nA Raiz quadrada de {} é igual a {:.3f}'.format(num,(s*2), num, pow(num,(1/2))))
#PARA FAZER A FORMAÇÃO DA RAIZ PARA FICA COM MENO NUMERO {:.NUMERO f}
