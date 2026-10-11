class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [nums[0]] 
        curr = nums[0]
        for i in range(1,len(nums)): 
            curr *= nums[i]
            prefix.append(curr)
        
        n = len(nums)
        prefix2 = [nums[n-1]]
        curr = nums[n-1]
        for i in range(len(nums)-2,-1,-1):
            curr *= nums[i]
            prefix2.append(curr)
        prefix2 = prefix2[::-1]
        #print(prefix,prefix2)
        ans = []
        for i in range(n):
            if i == 0:
                ans.append(prefix2[1])
            elif i == n-1:
                #print("meow")
                ans.append(prefix[n-2])
            else:
                ans.append(prefix[i-1]*prefix2[i+1])
            #print(ans)
        
        return ans 



            

        