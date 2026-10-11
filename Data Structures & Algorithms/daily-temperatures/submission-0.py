class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        stack = [(temperatures[0],0)]
        ans = [0 for _ in range(len(temperatures))]
        for i in range(1,len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                b = stack.pop()
                ans[b[1]] = i-b[1]
            stack.append((temperatures[i],i))
            
        return ans 
            
        