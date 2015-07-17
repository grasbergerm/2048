# Created by Matt Grasberger
import random
import copy

# Prints the board
def display_board():
    for row in board:
        for item in row:
            print("{:4}".format(item),end="  ")
        print()
        print()
# Randomly places a 2 or 4 after the player makes a move
def place_new():
    if has_free():
        placed = False
        while(placed == False):
            randomRow = random.randint(0,3)
            randomCol = random.randint(0,3)
            if board[randomRow][randomCol] == ".":
                randNum = random.randint(0,10)
                if randNum < 3:
                    board[randomRow][randomCol] = "4"
                else:
                    board[randomRow][randomCol] = "2"
                placed = True

# Rotates the board 90 degrees
def rotate_board():
    copyBoard = copy.deepcopy(board)
    for i in range(3,-1,-1):
        for j in range(3,-1,-1):
            board[i][j] = copyBoard[j][i]
    copyBoard = copy.deepcopy(board)
    for i in range(0,4):
        board[i] = copyBoard[i][::-1]

# Checks to see if there's a free space
def has_free():
    for row in board:
        for item in row:
            if item == "2048":
                display_board()
                print("You won!!!")
                quit()
    for row in board:
        for item in row:
            if (item == "."):
                return True
    return False

# Checks to see if there's a possible move
def possible_move():
    for row in board:
        for i in range(0,len(row)-1,1):
            if row[i] == row[i+1]:
                return True
    for i in range(3,0,-1):
        for j in range(3,-1,-1):
            if board[i][j] == board[i-1][j]:
                return True
    return False
# Shifts the board to the left
def shift_left():
    for row in board:
        # Combines like numbers
        for i in range(0,len(row)-1,1):
            if row[i] == ".":
                pass
            else:
                j = 1
                while(i+j < 3 and row[i+j] == "."):
                    j += 1
                if row[i+j] != "." and row[i] == row[i+j]:
                    row[i] = str(int(row[i]) + int(row[i+j]))
                    row[i+j] = "."
                else:
                    k = 1
                    while(i-k > 0 and row[i-k] == "."):
                        row[i-1] = row[i]
                        row[i] = "."
                        k += 1
        # Shifts numbers down after combining
        for iteration in range(3):
            for i in range(3,-1,-1):
                if row[i] == ".":
                    pass
                else:
                    k = 1
                    l = i
                    while(l-k >= 0 and row[l-k] == "."):
                        row[l-k] = row[l]
                        row[l] = "."
                        l -= 1

# An allowed move must change the board
def invalid_move():
    print("Not an acceptable move!")
# Main
if __name__ == '__main__':
    # Test board
    #board=[["2","4","128","4"],["16","32","8","2"],["4","64","4","16"],["2","128","8","4"]]
    # Blank board
    board=[[".",".",".","."],[".",".",".","."],[".",".",".","."],[".",".",".","."]]
    place_new()
    display_board()
    while(has_free() or possible_move()):
        move = input("Enter a move (WASD) \n")
        if move == "w":
            checkBoard = copy.deepcopy(board)
            rotate_board()
            rotate_board()
            rotate_board()
            shift_left()
            rotate_board()
            if checkBoard == board:
                invalid_move()
                display_board()
            else:
                place_new()
                display_board()
        elif move == "a":
            checkBoard = copy.deepcopy(board)
            shift_left()
            if checkBoard == board:
                invalid_move()
                display_board()
            else:
                place_new()
                display_board()
        elif move == "s":
            checkBoard = copy.deepcopy(board)
            rotate_board()
            shift_left()
            rotate_board()
            rotate_board()
            rotate_board()
            if checkBoard == board:
                invalid_move()
                display_board()
            else:
                place_new()
                display_board()
        elif move == "d":
            checkBoard = copy.deepcopy(board)
            rotate_board()
            rotate_board()
            shift_left()
            rotate_board()
            rotate_board()
            if checkBoard == board:
                invalid_move()
                display_board()
            else:
                place_new()
                display_board()
        else:
            print("Please enter w, a, s, or d.")
    print("Game Over!")
