class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] >= 1:
                return 1
            return 0
        i = 0 
        new_range = nums[i]
        new_start = i
        counter = 1
        if nums[0] >= len(nums)-1:
            return 1
        for i in range(len(nums)):
            if i == new_start:
                new_jump = 0
                for j in range(i+1,i+nums[i]+1):
                    if nums[j]+j > new_jump:
                        new_jump = nums[j]+j
                        new_start = j
                        if new_jump >= len(nums)-1:
                            return counter + 1
                        new_start = j 
                counter += 1

            #print(new_start)
        return False