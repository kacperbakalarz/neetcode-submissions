class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = [i]
            else:
                hash_map[nums[i]].append(i)

        for num in nums:
            tr = target - num
            #print(hash_map)
            if tr == num:
                if len(hash_map[tr]) >= 2:
                    ans = [hash_map[tr][0],hash_map[tr][1]]
                    return sorted(ans)
            else:
                if tr in hash_map:
                        print(hash_map[tr])
                        ans = [hash_map[tr][0],hash_map[num][0]]
                        return sorted(ans)