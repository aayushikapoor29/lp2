# all possible solns
def solve(n):
    board = [-1]*n  # [-1 -1 -1 -1]
    solutions = []   # to find

    # to check which col is safe for the row
    def is_safe(row, col):
        for i in range(row):
            if(board[i]==col or abs(board[i]-col) == abs(i - row)):
                return False  # combination discard
        return True  # combination is possible
    
    # for arrangement
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row+1)
                board[row] = -1

    backtrack(0)
    return solutions


# our output looks like a chess board
def print_solution(x):
    for sol in x:
        for row in sol:
            print('.'*row + 'Q' + '.'*(len(sol)-row-1))
        print()


# main code
n = 4 
solutions = solve(n)
print("Total solns are: ",len(solutions))
print_solution(solutions)