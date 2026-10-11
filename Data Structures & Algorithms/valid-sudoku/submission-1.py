class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        
        #rows

        for i in range(n):
            hash_map = [0 for _ in range(10)]
            for j in range(n):
                if board[i][j] != ".":
                        check = int(board[i][j])
                        hash_map[check] += 1
                        if hash_map[check] == 2:
                            return False

        for i in range(n):
            hash_map = [0 for _ in range(10)]
            for j in range(n):
                if board[j][i] != ".":
                        check = int(board[j][i])
                        hash_map[check] += 1
                        if hash_map[check] == 2:
                            return False

        squares = [ ((0,1,2),(0,1,2)), ((0,1,2),(3,4,5)), ((0,1,2),(6,7,8)), 
                    ((3,4,5),(0,1,2)), ((3,4,5),(3,4,5)), ((3,4,5),(6,7,8)),
                    ((6,7,8),(0,1,2)), ((6,7,8),(3,4,5)), ((6,7,8),(6,7,8))]

        for square in squares:
            range_i = square[0]
            range_j = square[1]
            hash_map = [0 for _ in range(10)]
            for i in (range_i):
                for j in (range_j):
                    #print(i,j)
                    if board[i][j] != ".":
                        check = int(board[i][j])
                        hash_map[check] += 1
                        if hash_map[check] == 2:
                            return False

        
        return True

