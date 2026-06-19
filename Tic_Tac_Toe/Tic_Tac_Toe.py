player = 0
ai = 0
# Rules:
# Win = 2 points
# Draw = 1 point each
# Loss = 0 points


def show_board():
    print()
    print("0 | 1 | 2")
    print("-" * 9)
    print("3 | 4 | 5")
    print("-" * 9)
    print("6 | 7 | 8")


def print_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("-" * 9)
    print(board[3], "|", board[4], "|", board[5])
    print("-" * 9)
    print(board[6], "|", board[7], "|", board[8])


def user_move(board, zero_cross):
    while True:
        try:
            move = int(input("Enter your position of move (0-8): "))

            if move < 0 or move > 8:
                print("Enter a position between 0 and 8")
                continue

            if board[move] == " ":
                board[move] = zero_cross
                break
            else:
                print("Position is already filled !!")

        except ValueError:
            print("Please enter a valid number.")


def ai_choice(zero_cross):
    if zero_cross == "X":
        return "O"
    else:
        return "X"


def check_win(board, zero_cross):
    win_patterns = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for pattern in win_patterns:
        if (board[pattern[0]] == zero_cross and
            board[pattern[1]] == zero_cross and
            board[pattern[2]] == zero_cross):
            return True

    return False


def check_result(board,ai_zero_cross,zero_cross):
    if check_win(board,ai_zero_cross):
        return "AI"
    
    if check_win(board,zero_cross):
        return "PLAYER"
    
    if " " not in board:
        return "DRAW"
    
    return None

def minimax(board,is_maximizing,zero_cross,ai_zero_cross):
    result = check_result(board,ai_zero_cross,zero_cross)

    if result=="AI":
        return 1
    
    if result=="PLAYER":
        return -1
    
    if result=="DRAW":
        return 0
    
    if is_maximizing:
        best_score = -100

        for i in range(9):
            if board[i]==" ":
                board[i]=ai_zero_cross
                score = minimax(board,False,zero_cross,ai_zero_cross)

                board[i] = " "

                best_score = max(best_score,score)
        return best_score

    else:
        best_score = 100

        for i in range(9):
            if board[i]==" ":
                board[i]=zero_cross
            
                score = minimax(board,True,zero_cross,ai_zero_cross)

                board[i] = " "

                best_score = min(best_score,score)
        return best_score


def ai_move(board,ai_zero_cross,zero_cross):
    best_score = -100
    best_move = -1

    for i in range(9):
        if board[i]==" ":
            board[i]=ai_zero_cross

            score = minimax(board,False,zero_cross,ai_zero_cross)
            board[i] = " "

            if score>best_score:
                best_score = score
                best_move = i

    board[best_move] = ai_zero_cross


def show_points(player, ai):
    print("\nScoreboard")
    print("-" * 20)
    print(f"Player = {player}")
    print(f"AI     = {ai}")
    print("-" * 20)


print("-" * 15)
print(" TIC TAC TOE ")
print("-" * 15)
print("\nRules:- ")
print("1.For winning +2 points")
print("2.For Losing 0 points")
print("3.For Draw +1 points are awarded to both AI and Player\n")

while True:
    zero_cross = input("Enter your symbol (O/X): ").upper()

    if zero_cross in ["O", "X"]:
        break

    print("Enter either O or X\n")

ai_zero_cross = ai_choice(zero_cross)

while True:

    print("\n===== MENU =====")
    print("1. View board positions")
    print("2. Play")
    print("3. View points board")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice")
        continue

    if choice == 1:
        show_board()

    elif choice == 2:

        board = [" " for i in range(9)]

        print("\nYour Symbol =", zero_cross)
        print("AI Symbol =", ai_zero_cross)

        while True:

            user_move(board, zero_cross)
            print_board(board)

            if check_win(board, zero_cross):
                print("\nYou won !!")
                player += 2
                break

            if " " not in board:
                print("\nIt is a Draw !!")
                player += 1
                ai += 1
                break

            ai_move(board,ai_zero_cross,zero_cross)

            print("\nAI Move:")
            print_board(board)

            if check_win(board, ai_zero_cross):
                print("\nYou lost !!")
                ai += 2
                break

            if " " not in board:
                print("\nIt is a Draw !!")
                player += 1
                ai += 1
                break

        show_points(player, ai)

    elif choice == 3:
        show_points(player, ai)

    elif choice == 4:
        print("Thank you for playing !!")
        print("See you soon !!")
        exit=int(input("Press 4 again to exit..."))
        if exit==4:
            break

    else:
        print("Invalid Choice")
