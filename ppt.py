import random

print('-=' * 30)
print('Suas opções são:\n [ 1 ] Pedra\n [ 2 ] Papel\n [ 3 ] Tesoura')
print('-=' * 30)
player = int(input('Qual sua jogada: '))
pc = random.randint(1,3)
if pc == 1: 
    if player == 1:
        print('Empate')
    elif player == 2:
        print('O player venceu')
    elif player == 3:
        print('O pc venceu')
elif pc == 2:
    if player == 1:
        print('O pc venceu')
    elif player == 2:
        print('Empate')
    elif player == 3:
        print('O player venceu')
elif pc == 3:
    if player == 1:
        print('O player venceu')
    elif player == 2:
        print('O pc venceu')
    elif player == 3:
        print('Empate')
else:
    print('erro')