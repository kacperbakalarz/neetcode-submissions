class Solution:
    def isHappy(self, n: int) -> bool:
        hash_dic = {}
        def square_sum(n1):
            ans = 0
            while n1 > 0:
                ans += math.pow(n1 % 10,2)
                n1 //= 10
            return ans 
        while n != 1:
            new_n = square_sum(n)
            if new_n not in hash_dic:
                hash_dic[new_n] = 1
            else:
                return False
            n = new_n
        return True