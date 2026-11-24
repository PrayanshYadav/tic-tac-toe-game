
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

current_player = "X"


def display_board():
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


def check_winner():
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:
        if (board[combination[0]] == board[combination[1]] ==
                board[combination[2]]):
            return True

    return False


def check_draw():
    return all(position in ["X", "O"] for position in board)


def make_move():
    global current_player

    while True:
        try:
            position = int(input(f"Player {current_player}, enter position (1-9): "))

            if position < 1 or position > 9:
                print("Invalid position! Choose between 1 and 9.")
                continue

            if board[position - 1] in ["X", "O"]:
                print("Position already occupied! Choose another position.")
                continue

            board[position - 1] = current_player
            break

        except ValueError:
            print("Invalid input! Please enter a number.")


def switch_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def play_game():
    print("================================")
    print("       TIC TAC TOE GAME")
    print("================================")
    print("Player 1: X")
    print("Player 2: O")

    while True:
        display_board()
        make_move()

        if check_winner():
            display_board()
            print(f"Congratulations! Player {current_player} wins!")
            break

        if check_draw():
            display_board()
            print("The game is a draw!")
            break

        switch_player()


play_game()
