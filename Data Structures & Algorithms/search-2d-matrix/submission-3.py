class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])-1
        if len(matrix) == 1:
            row = 0
        else:

            left = 0
            right = m-1
            row = float("inf")  
            i = 0 
            while left <= right:
                if matrix[left][0] == target or matrix[right][0] == target or matrix[left][n] == target or matrix[right][n] == target:
                    return True 
                if matrix[left][0] < target < matrix[left][n]:
                    row = left
                    break
                if matrix[right][0] < target < matrix[right][n]:
                    row = right
                    break 
                
                mid = (left + right) // 2
                if target < matrix[mid][0]:
                    right = mid - 1
                elif target > matrix[mid][n]:
                    left = mid + 1
                else:
                    row = mid
                    break
        if row == float('inf'):
            return False
        if len(matrix[row]) == 1:
            return matrix[row][0] == target
        
        #print(row)
        left = 0
        right = n
        while left <= right:
            mid = (left + right) // 2

            if  matrix[row][mid] == target:
                return True

            if matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

