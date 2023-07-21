from random import randint
from time import sleep
opcoes = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('Escolha sua opção:')
print('''
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')
jogador = int(input('Digite sua escolha: '))
print('PEDRA...')
sleep(3)
print('PAPEL...')
sleep(2)
print('TESOURA!!!')
sleep(1)
print('='*30)
print('O computador escolheu {}'.format(opcoes[computador]))
print('Sua escolha foi {}'.format(opcoes[jogador]))
print('='*30)
if computador == 0: #computador escolheu Pedra
    if jogador == 0:
        print('Empate!!!')
    elif jogador == 1:
        print('Parabéns você ganhou!!!')
    elif jogador == 2:
        print('Que pena você perdeu!!!')
    else:
        print('Jogada inválida!!! Jogue novamente!!!')
elif computador == 1: #computador escolheu Papel
    if jogador == 0:
        print('Que pena você perdeu!!!')
    elif jogador == 1:
        print('Empate!!!')
    elif jogador == 2:
        print('Parabéns você ganhou!!!')
    else:
        print('Jogada inválida!!! Jogue novamente!!!')
elif computador == 2: #computador escolheu Tesoura
    if jogador == 0:
        print('Parabéns você ganhou!!!')
    elif jogador == 1:
        print('Que pena você perdeu!!!')
    elif jogador == 2:
        print('Empate!!!')
    else:
        print('Jogada inválida!!! Jogue novamente!!!')

