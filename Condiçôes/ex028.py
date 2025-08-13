import random
import time
num = random.randint(0, 5)  # Gera um número aleatório entre 0 e 5
print("-=-" * 20)
print("Vou pensar em um numero entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)
jgd = int(input("Digite um numero 0 a 5: ")) # O usuário tenta adivinhar o número
if jgd == num:
    print("PROCESSANDO...")
    time.sleep(2)  # Pausa de 2 segundos para aumentar a expectativa
    print(f"Parabéns, você acertou!{num}")
else:
    print("PROCESSANDO...")
    time.sleep(2)  # Pausa de 2 segundos para aumentar a expectativa
    print(f"Você errou! Eu pensei no número {num} e não no {jgd} !")
    