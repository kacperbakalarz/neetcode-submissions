class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for i in range(len(nums)):
            new_target = target - nums[i]
            if new_target in hash_map:
                ans = (hash_map[new_target],i)
                return sorted(ans)
            hash_map[nums[i]] = i 