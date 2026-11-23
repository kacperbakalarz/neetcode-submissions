class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxi = max(nums)
        tab = []
        for i in range(maxi+1):
            tab.append(i)
        

        diff = list(set(tab) - set(nums))

        if not diff:
            return maxi+1
        else:
            return diff[0]