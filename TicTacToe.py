import random

wins = '''123,456,789,147,258,369,753,159'''
counter = 1
player = 'X'
comp = False
game_on = True


def print_board():
    print('\n', wins[0], '|', wins[1], '|', wins[2], '\n', '----------',
          '\n', wins[4], '|', wins[5], '|', wins[6], '\n', '----------',
          '\n', wins[8], '|', wins[9], '|', wins[10], '\n')


def comp_str_match(compare1, compare2):
    global wins
    start = 0
    end = 3

    # Checks each str segment for winning positions (O,O,#) (X,#,X) etc.
    while start < 30:
        wins_seg = wins[start:end]

        if wins_seg.count(compare1) == 2 and wins_seg.count(compare2) < 1:
            # Validates remaining spot as a valid move: (X,3,X)
            for i in wins_seg:
                if i in str('123456789'):
                    return i
        else:
            start += 4
            end += 4


def move(player):
    global wins, comp, counter
    invar = '0'

    if player == 'O':
        while invar not in wins and invar not in str(' ,XO'):
            invar = input(f'{player} select a position number: ')

    # Computer Moves
    elif comp:
        # Checks for winning positions for X or O.
        if comp_str_match('X', 'O'):
            invar = comp_str_match('X', 'O')
        elif comp_str_match('O', 'X'):
            invar = comp_str_match('O', 'X')

        else:
            while invar not in wins and invar not in str(' ,XO'):
                invar = str(random.randint(1, 10))
        print("Computer Moved...")
    # X player Moves
    else:
        while invar not in wins and invar not in str(' ,XO'):
            invar = input(f'{player} select a position number: ')

    wins = wins.replace(invar, player)


def check_winner(player):
    global game_on, wins

    if wins.find(f'{player}{player}{player}') != -1:
        print(f'{player} Wins!')
        game_on = False

    if counter == 10 and game_on:
        print("It's a tie!")
        game_on = False


def main():
    global game_on, counter, comp

    print('\n', 'TIC TAC TOE!', '\n')
    print_board()

    menu = '0'
    while menu not in str('1') and menu not in str('2'):
        menu = input('How many players (1 or 2)? ')
    if menu == '1':
        comp = True

    # Game loop
    while game_on:
        if counter % 2 != 0:
            player = 'X'
        else:
            player = 'O'

        move(player)
        counter += 1
        print_board()
        check_winner(player)


main()
