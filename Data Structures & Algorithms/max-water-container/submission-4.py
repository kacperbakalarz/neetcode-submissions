class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        maxi = 0
        while i < j:
            area = (j-i) * min(heights[i],heights[j])
            maxi = max(maxi,area)
            if heights[j] >= heights[i]:
                i += 1
            else:
                j -= 1
        return maxi
            