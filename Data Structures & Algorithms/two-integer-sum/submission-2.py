class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = {}
  
        for i in range(len(nums)):
            num = nums[i]
            if nums[i] not in hash1:
                hash1[num] = i
            else:
                if num*2 == target:
                    return [hash1[num],i]
        
        for num in nums:
            if target - num in hash1 and num*2 != target:
                return [hash1[num],hash1[target-num]]



