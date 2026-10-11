class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        nums = set(nums)
        ans = 0
        for num in nums:
            if num-1 not in nums:
                curr = 1
                tmp = num+1
                while tmp in nums:
                    curr += 1
                    tmp += 1
                ans = max(ans,curr)
            else:
                curr = 0
        return ans 


        

        