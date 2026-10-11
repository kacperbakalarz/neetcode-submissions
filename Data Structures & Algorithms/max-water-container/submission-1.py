class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        ans = -float('inf')
        while i < j:
            ans = max(ans,(j-i)*min(heights[j],heights[i]))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return ans