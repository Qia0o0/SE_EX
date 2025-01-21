def is_win(game):
    # Check rows and columns
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] != ' ':
            return True
        if game[0][i] == game[1][i] == game[2][i] != ' ':
            return True
    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] != ' ':
        return True
    if game[0][2] == game[1][1] == game[2][0] != ' ':
        return True
    return False


def print_board(game):
    for row in game:
        print(" | ".join(row))
        print("-" * 5)


def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]  # Tic-tac-toe board
    players = ['X', 'O']
    turn = 0  # Player 1 starts

    print("Tic-Tac-Toe Game")
    print("X = Player 1")
    print("O = Player 2")

    for n in range(9):
        print_board(game)
        print(f"Player {turn + 1} ({players[turn]}): Which cell to mark? (i:[1-3], j:[1-3]): ")
        i, j = map(int, input().split())
        i -= 1
        j -= 1

        if game[i][j] != ' ':
            print("This cell is already occupied!")
            continue

        game[i][j] = players[turn]

        if is_win(game):
            print_board(game)
            print(f"Player {turn + 1} ({players[turn]}) wins!")
            return

        turn = 1 - turn  # Switch turns

    print_board(game)
    print("It's a tie!")


if __name__ == "__main__":
    main()
