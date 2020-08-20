import csv
import random

wins = '''123,456,789,147,258,369,753,159'''
cur_game = [0]*9
game_moves = []
counter = 1
num_games = 0
o_wins = []
x_wins = []
x_score = 0
o_score = 0
player = 'X'
comp = False
game_on = True


def print_board():
    print('\n', wins[0], '|', wins[1], '|', wins[2], '\n', '----------',
          '\n', wins[4], '|', wins[5], '|', wins[6], '\n', '----------',
          '\n', wins[8], '|', wins[9], '|', wins[10], '\n')


def move(player):
    global wins, counter, cur_game
    invar = '0'
    # Computer Moves
    if comp:
        play_move = comp_str_match('X', 'O')
        if comp_str_match('X', 'O'):
            invar = check_valid(comp_str_match('X', 'O'))
        elif comp_str_match('O', 'X'):
            invar = check_valid(comp_str_match('O', 'X'))

        else:
            while invar not in wins and invar not in str(' ,XO'):
                invar = str(random.randint(1, 10))

    # Player Moves
    else:
        while invar not in wins and invar not in str(' ,XO'):
            invar = input('{} select a position number: '.format(player))

    wins = wins.replace(invar, player)
    cur_game[int(invar) - 1] = counter


def comp_str_match(compare1, compare2):
    global wins
    start = 0
    end = 3

    while start < len(wins):
        if wins[start:end].count(compare1) == 2 and wins[start:end].count(compare2) < 1:
            return(wins[start:end])
        else:
            start += 4
            end += 4


def check_valid(play_move):
    for i in play_move:
        if i in str('123456789'):
            return i


def check_winner(player):
    global game_on, wins, cur_game, num_games, x_score, o_score, x_wins, o_wins

    if wins.find('{}{}{}'.format(player, player, player)) != -1:
        if player == 'X':
            print('current check winner', cur_game)
            x_score += 1
            backtrac(player)
        else:
            o_score += 1
            # Going to use X to start. Need winning positions.
            # backtrac(player)
        num_games += 1
        game_on = False

    if counter == 10 and game_on:
        print("It's a tie!")
        num_games += 1
        game_on = False


def backtrac(player):
    global cur_game, all_games, x_wins, o_wins
    print(cur_game)
    # Need to specify X winning positions. Can only use X turns (max
    # cur_game%2 != 0 and max cur_game != 0)
    for i in range(len(cur_game)):
        print('cur game', cur_game)
        max_pos = cur_game.index(max(cur_game))
        max_value = max(cur_game)

        # Checks to see if odd(X). If so, change to 0 and set the temp_y.
        if max(cur_game) % 2 != 0 and max(cur_game) != 0:
            cur_game[max_pos] = 0
            one_hot = []
            one_hot_y = []
            temp_y = max_pos+1  

            # Goes over temp_game and sets to onehot encoding None(0,0,0) or
            # X(0,0,1) or O(0,1,0).
            for i in range(len(cur_game)):
                if cur_game[i] == 0:
                    one_hot.extend([0, 0])
                    #print('tried none')
                elif cur_game[i] % 2 != 0:
                    one_hot.extend([0, 1])
                    #print('tried odd')
                elif cur_game[i] % 2 == 0:
                    one_hot.extend([1, 0])
                    #print('tried even')
                else:
                    print('ENCODING ERROR')
                     
            if player == 'X':
                x_wins.append(one_hot + [temp_y])
                #print('x_wins', x_wins)
            if player == 'O':
                o_wins.append(one_hot + [temp_y])
        elif max(cur_game) % 2 == 0 and max(cur_game) != 0 and max(cur_game) != 1:
            cur_game[max_pos] = 0
        else:
            print('I cant do that Hal!')


def reset_game():
    global game_on, wins, counter, cur_game

    game_on = True
    wins = '''123,456,789,147,258,369,753,159'''
    cur_game = [0]*9
    counter = 1


def main():
    global game_on, num_games, counter, comp, x_score, o_score

    # Gives the number of games generate:
    while num_games < 100000:
        while game_on:
            if counter % 2 != 0:
                player = 'X'
            else:
                player = 'O'

            move(player)
            counter += 1
            check_winner(player)
        reset_game()
    print('\n O wins', o_score, '\n X wins', x_score)
    print('Over {} games, X won: '.format(
        num_games), x_score, 'and O won: ', o_score)


# Game menu:
menu = '1'
comp = True

print('TIC TAC TOE!', '\n')
print_board()

main()

# Output results to the .csv file
with open("x_wins.csv", 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerows(x_wins)
with open("o_wins.csv", 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerows(o_wins)
print("\n\n...DONE...")
