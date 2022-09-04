# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.


import os
def clear_screen():
    os.system('clear')


board = list(range(1,10))


def draw_board(val): 
    print("\n") 
    print("\t     |     |") 
    print("\t  {}  |  {}  |  {}".format(val[0], val[1], val[2])) 
    print('\t_____|_____|_____') 
  
    print("\t     |     |") 
    print("\t  {}  |  {}  |  {}".format(val[3], val[4], val[5])) 
    print('\t_____|_____|_____') 
  
    print("\t     |     |") 
  
    print("\t  {}  |  {}  |  {}".format(val[6], val[7], val[8])) 
    print("\t     |     |") 
    print("\n") 

def draw_tablo(tmp): 
    print("\t--------------------------------") 
    print(f"\t|       Игрок {tmp} победил!       |") 
    print("\t--------------------------------") 


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Сейчас ход " + player_token + ", введите цифру: ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод.")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы сделать ход.")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def game(board):
    counter = 0
    win = False
    while not win:
        clear_screen()
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                clear_screen()
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)
    draw_tablo(tmp)

game(board)