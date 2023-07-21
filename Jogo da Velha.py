from random import randrange

def display_board(board):
    #A função aceita um parâmetro contendo o status atual do quadro e mostra para o usuário.
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[0][0] + '   |   ' + board[0][1] + '   |   ' + board[0][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[1][0] + '   |   ' + board[1][1] + '   |   ' + board[1][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[2][0] + '   |   ' + board[2][1] + '   |   ' + board[2][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')

def enter_move(board):
    #A função recebe status atual do quadro, pergunta ao usuário sobre sua jogada, verifica a entrada e atualiza o quadro de acordo com a decisão do usuário.
    while True:
        move = int(input('Por favor escolha um número do quadro, entre 1-9: '))
        # Verifica se a opção escolhida está disponível e se é a válida
        if move < 1 or move > 9:
            print('Opção digitada não é válida')
            continue
        elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
            print('Desculpe, Mas a opção escolhida já está ocupada. Por favor escolha outra opção!!!')
            continue
        # Vai passa por cada linha e coluna do quadro até encontrar a opção escolhida pelo usuário    
        for row in range(0,3): # for utilizado no lugar de todos os ilif
            for column in range(0,3):
                if board[row][column] == str(move):
                    board[row][column] = 'O'
        # elif move == 1:
        #     board[0][0] = 'O'
        # elif move == 2:
        #     board[0][1] = 'O'
        # elif move == 3:
        #     board[0][2] = 'O'
        # elif move == 4:
        #     board[1][0] = 'O'
        # elif move == 6:
        #     board[1][2] = 'O'
        # elif move == 7:
        #     board[2][0] = 'O'
        # elif move == 8:
        #     board[2][1] = 'O'
        # elif move == 9:
        #     board[2][2] = 'O'
        break

def make_list_of_free_fields(board):
    # A função navega pelo quadro e constrói uma lista de todas as opções livres;
    # a lista consiste em tuplas, enquanto cada tupla é um par de números de linha e coluna.
    global free_squares
    free_squares = [ ]
    for row in range(0,3): 
        for column in range(0,3):
            if board[row][column] == 'O' or board[row][column] == 'X':
                pass
            else:
                free_squares.append(([row],[column]))
    #print(free_squares)

def victory_for(board, sign):
    # A função analisa o status do quadro para verificar se o jogador usando 'O's ou 'X's ganhou o jogo
    if sign == 'O':
        print('Verificando se você é o vencedor!')
    else:
        print('Verificando se o computador é o vencedor!')
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True #print('PARABÉNS!!! Jogador ',sign,' você é o vencedor')
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True #print('PARABÉNS!!! Jogador ',sign,' você é o vencedor')
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True #print('PARABÉNS!!! Jogador ',sign,' você é o vencedor')
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True #print('PARABÉNS!!! Jogador ',sign,' você é o vencedor')
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True #print('PARABÉNS!!! Jogador ',sign,' você é o vencedor')
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True #print('PARABÉNS!!! Jogador ',sign,' você é o vencedor')
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True #print('PARABÉNS!!! Jogador ',sign,' você é o vencedor')
    elif board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
        return True #print('PARABÉNS!!! Jogador ',sign,' você é o vencedor')
    else:
        print('Ainda não temos um vencedor')

def draw_move(board):
    # A função desenha a jogada do computador e atualiza o quadro.
    while True:
        row = randrange(3) # Pega uma linha aleatória, entre 0 e 2
        column = randrange(3) # Pega uma coluna aleatório, entre 0 e 2
        if ([row],[column]) not in free_squares:
            # Se o conjunto de linha e coluna não estiver livre, refaz o processo no loop
            continue
        else:
            # Caso esteja livre vai usar a opção livre e retornar, saindo do loop
            board[row][column] = 'X'
            return

board = [['1','2','3'],['4','X','6'],['7','8','9']] # quadro inicial da partida
numberofmove = 1 # número de jogadas realizadas
humano = 'O'
computador = 'X'
print('Óla, Seja Bem Vindo ao Jogo da Velha!!!')
print('Aqui está o quadro atual do nosso jogo')
display_board(board) # Montagem do quadro
print('')
while numberofmove < 9: # enquanto o número de jogadas forem inferior a 9 o jogo continua
# Jogada do usuário
    enter_move(board)
    numberofmove += 1
    display_board(board)
    if victory_for(board,humano) == True: # Se o jogador fechou algumas das posibilidades, finaliza com sua vitória
        print('Você derrotou o computador, Você é o CARA! Uhuuuuu!!!')
        break
    else:
        print('Aqui está as opções que não foram assinaladas ainda: ')
        make_list_of_free_fields(board)
        print()
        display_board(board)
# Jogada do computador
    print()
    print('Agora é a vez do computador fazer a escolha!')
    draw_move(board)
    numberofmove += 1
    display_board(board)
    print()
    if victory_for(board,computador) == True: # Se o computador fechou uma das possibilidades, finaliza com sua vitória
        print('O computador venceu!!!, Tenha mais sorte na próxima vez!')
        break
    else:
        print('Aqui está as opções que não foram assinaladas ainda: ')
        make_list_of_free_fields(board)
        print()
        display_board(board)
else:
    # preencheu todas as opções mas não teve um vencedor
    print('Nós temos um empate, este é um jogo de compadres!')

print('Obrigado pela partida!')

#display_board(board)
#enter_move(board)
#display_board(board)
#make_list_of_free_fields(board)
#victory_for(board,humano)
#victory_for(board,computador)
#draw_move(board)
#victory_for(board,humano)
#victory_for(board,computador)
#display_board(board)