class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash1 = {}
        for num in nums:
            if num not in hash1:
                hash1[num] = 1
            else:
                return True
        return False

