import os
import inquirer

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

turn = 'O'

moves = {
    'O': [],
    'X': []
}

default_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def toggle_turn():
    global turn
    turn = 'X' if turn == 'O' else 'O'

def remaining_moves():
    available_moves = default_moves.copy()
    for move in moves['O'] + moves['X']:
        available_moves.remove(move)
    
    return available_moves

def display_board():
    display_moves = []

    for i in range(1, len(default_moves) + 1):
        display_moves.append('O' if i in moves['O'] else ('X' if i in moves['X'] else i))

    for i in range(3):
        print(f"\t\t{display_moves[3 * i + 0]} | {display_moves[3 * i + 1]} | {display_moves[3 * i + 2]}")
        if i < 2:
            print("\t\t---------")    

    print()

def check_winner():
    winning_combinations = [
        [1, 2, 3],
        [1, 4, 7],
        [1, 5, 9],
        [2, 5, 8],
        [3, 6, 9],
        [3, 5, 7],
        [4, 5, 6],
        [7, 8, 9],
    ]

    message = ''

    for combination in winning_combinations:
        if combination[0] in moves['O'] and combination[1] in moves['O'] and combination[2] in moves['O']:
            message = "Player O wins!\n"
            return message
        elif combination[0] in moves['X'] and combination[1] in moves['X'] and combination[2] in moves['X']:
            message = "Player X wins!\n"
            return message

    if len(remaining_moves()) == 0:
        message = "Game is a Draw!\n"
        return message
    
def play_again():
    question = [
        inquirer.List('choice',
            message=f"Do you want to play again?",
            choices=[
                ('Yes',True),
                ('No',False),
            ],
        ),
    ]

    answer = inquirer.prompt(question)

    if answer['choice']:
        reset_values()
    else:
        print("Thanks for playing!")
        exit(0)
    
def reset_values():
    global turn
    global moves

    turn = 'O'

    moves = {
        'O': [],
        'X': []
    }

def ask_question():
    available_moves = remaining_moves()

    question = [
        inquirer.List('choice',
            message=f"Select Your Move: {turn}",
            choices=available_moves,
        ),
    ]

    answer = inquirer.prompt(question)

    choice = answer['choice']

    return choice


def play_move():
    global moves

    cls()
    display_board()

    choice = ask_question()

    moves[turn].append(choice)

    game_over = check_winner()

    if game_over:
        cls()
        display_board()
        print(game_over)
        play_again()
    else:
        toggle_turn()

while True:
    play_move()