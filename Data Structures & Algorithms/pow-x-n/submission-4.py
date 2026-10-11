class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1.00000:
            return 1.00000
        if x == -1.00000 and n%2 == 1:
            return -1.00000
        if x == -1.00000 and n%2 == 0:
            return 1.00000
        if n == 0:
            return 1
        if n > 0:
            num = 1
            for i in range(n):
                num *= x
            return num
        if n < 0:
            num = 1
            for i in range(abs(n)):
                num *= x
                #print(1/num)
                if 1/num == 0.00000:
                    return 1/num
            return 1/num