tab = int(input('Digite um número para ver sua tabuada:'))
print('tabuada do número {}'.format(tab))
for i in  range(1, 11):
    res = tab * i
    print('{} x {:2} = {:2}'.format(tab, i, res))

num = int(input('Digite um número para ver sua tabuada:'))
print('-'*12)
print('{} X {:2} = {}'.format(num, 1, num*1))
print('{} X {:2} = {}'.format(num, 2, num*2))
print('{} X {:2} = {}'.format(num, 3, num*3))
print('{} X {:2} = {}'.format(num, 4, num*4))
print('{} X {:2} = {}'.format(num, 5, num*5))
print('{} X {:2} = {}'.format(num, 6, num*6))
print('{} X {:2} = {}'.format(num, 7, num*7))
print('{} X {:2} = {}'.format(num, 8, num*8))
print('{} X {:2} = {}'.format(num, 9, num*9))
print('{} X {:2} = {}'.format(num, 10, num*10))
print('-'*12)