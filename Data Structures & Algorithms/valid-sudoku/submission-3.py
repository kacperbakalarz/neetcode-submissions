class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = set()
        col_check = set()
        for i in range(len(board)):
            row_check = set()
            col_check = set()
            for j in range(len(board)):
                    #rint(j,i)
                    if board[i][j] != "." :
                        if board[i][j] in row_check:
                            #print(i,j)
                            return False
                        else:
                            row_check.add(board[i][j])
                    if board[j][i] != ".":
                        if board[j][i] in col_check:
                            return False
                        else:
                            col_check.add(board[j][i])
        

        squares = [(0,1,2),(3,4,5),(6,7,8)]
        for x in squares:
            for y in squares:
                square_check =set()
                #print(x,y)
        
                for i in x:
                    for j in y:
                        #print(i,j)
                        if board[i][j] != ".":
                            if board[i][j] in square_check:
                                #print(square_check)
                                return False
                            else:
                                square_check.add(board[i][j])
        return True
            
                