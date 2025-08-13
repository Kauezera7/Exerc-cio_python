num = (int(input('Digite um número: '))) 
if num % 2 == 0: # Verifica se o número é par
                 # Se for par, imprime a mensagem em verde
    print(f'\033[32mO número {num} é par!')
    print(f'O número {num} é par!')
else:
    print(f'O número {num} é ímpar!')
