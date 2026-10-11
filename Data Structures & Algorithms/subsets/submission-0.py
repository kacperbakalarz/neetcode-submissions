class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        def subset(array,new):
            new_array = []
            tmp = []
            for each in array:
                tmp = list(each)
                tmp.append(new)
                new_array.append(tmp)
            for each in new_array:
                array.append(each)
        
        for num in nums:
            subset(ans,num)

        return ans
                