class Solution:
    def reverse(self, x: int) -> int:
        revers = 0
        if x < 0:
            flag = 1
        else:
            flag = 0
        x = abs(x)
        while x > 0:
            revers += x%10
            revers *= 10
            x //= 10
        if flag == 1:
            revers = -revers
        revers = revers//10
        if revers > math.pow(2,31)-1 or revers < -math.pow(2,31):
            return 0
        return revers