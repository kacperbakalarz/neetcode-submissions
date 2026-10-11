class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for k in range(len(nums)):
            target = -nums[k]
            i = 0
            j = len(nums)-1
            suma = nums[i] + nums[j]
            while i < j and i != k and j != k:
                if suma == target:
                    trojka = tuple(sorted((nums[k], nums[i], nums[j])))
                    ans.append(trojka)
                    i += 1
                    j -= 1
                    
                elif suma < target:
                    i += 1
                else:
                    j -= 1
                suma = nums[i] + nums[j]
        #print(ans)
        return list(set(ans))