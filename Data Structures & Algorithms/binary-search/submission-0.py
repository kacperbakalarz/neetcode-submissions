class Solution:
    def search(self, nums: List[int], target: int) -> int:
        end = len(nums)-1
        start = 0
        pivot = len(nums)//2
        i = 0
        while start <= end: 
            if target > nums[pivot]:
                end = end 
                start = pivot+1
                pivot = (start+end)//2
            elif target < nums[pivot]:
                start = start 
                end = pivot-1
                pivot = (start+end)//2
            elif target == nums[pivot]:
                return pivot
            
        return -1 