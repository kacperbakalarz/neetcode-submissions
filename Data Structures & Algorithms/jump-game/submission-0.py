class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False 
        if len(nums) == 1:
            return True
        if len(nums) == 2:
            return nums[0] >= 1
        i = 0 
        new_range = nums[i]
        new_start = i
        for i in range(len(nums)):
            if i == new_start:
                new_jump = 0
                for j in range(i+1,i+nums[i]+1):
                    jump = j + nums[j]
                    #print(jump)
                    if jump > new_jump:
                        new_jump = j + nums[j]
                        new_start = j
                    if jump >= len(nums)-1:
                        return True 
                if  new_jump == 0:
                    return False
            #print(new_start)
        return False


        
