class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        sorted_dict = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))
        i = 0
        ans =[]
        for num in sorted_dict:
            ans.append(num)
            i += 1
            if i == k:
                return ans