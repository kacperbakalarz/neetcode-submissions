class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for num in nums:
            if num in dict1:
                dict1[num] += 1
            else:
                dict1[num] = 1
        
        dict1 = dict(sorted(dict1.items(), key=lambda x: x[1], reverse=True))
        ans = []
        for key in dict1:
            ans.append(key)
            if len(ans) == k:
                return ans
        return ans 