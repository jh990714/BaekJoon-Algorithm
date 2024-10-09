import sys

input = sys.stdin.readline

def checkBoard():
    x_cnt = board.count('X')
    o_cnt = board.count('O')

    if x_cnt > 5 or o_cnt > 4 or x_cnt < o_cnt:
        return False

    if x_cnt == o_cnt + 1:
        return 'X', 'O'
    elif x_cnt == o_cnt:
        return 'O', 'X'
    else:
        return False
        
def checkBingo(user):
    # 가로
    for i in range(0, 9, 3):
        if board[i] == user and board[i] == board[i+1] == board[i+2]:
            return True
    # 세로
    for i in range(3):
        if board[i] == user and board[i] == board[i+3] == board[i+6]:
            return True
    # 대각선
    if board[0] == user and board[0] == board[4] == board[8]:
        return True
    
    if board[2] == user and board[2] == board[4] == board[6]:
        return True
    
    return False

while True:
    board = input().rstrip()

    if board == "end":
        break

    result = checkBoard()

    if not result:
        print("invalid")
        continue

    win_user, lose_user = result

    if checkBingo(win_user) and not checkBingo(lose_user):
        print("valid")
    elif '.' not in board and not checkBingo(win_user) and not checkBingo(lose_user):
        print("valid")
    else:
        print("invalid")