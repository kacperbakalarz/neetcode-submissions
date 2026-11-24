class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        def counter(n):
            ans = 0
            for el in n:
                if el == '1':
                    ans += 1
            return ans
        for i in range(n+1):
            bins = (bin(i)[2:])
            ans.append(counter(bins))
        return ans

            

