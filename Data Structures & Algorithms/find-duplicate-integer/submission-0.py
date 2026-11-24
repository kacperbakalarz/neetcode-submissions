class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_map = dict()
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                return num