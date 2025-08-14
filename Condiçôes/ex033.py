pri = int (input('Primeiro valor: '))
seg = int (input('Segundo valor: '))
ter = int (input('Terceiro valor: '))
if pri > seg and pri > ter: # Verifica se o primeiro é o maior
    maior = pri 
elif seg > pri and seg > ter: # Verifica se o segundo é o maior
    maior = seg

print(f'O maior valor é {max(pri, seg, ter)}.')

if pri < seg and pri < ter: # Verifica se o primeiro é o menor
    menor = pri 
elif seg < pri and seg < ter: # Verifica se o segundo é o menor
    menor = seg
print(f'O menor valor é {min(pri, seg, ter)}.')