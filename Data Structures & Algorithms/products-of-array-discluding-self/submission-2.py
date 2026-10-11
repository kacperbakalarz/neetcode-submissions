class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full = 1
        for num in nums:
            full *= num

        tab = [full for _ in range(len(nums))]

        for i in range(len(nums)):
            if nums[i] == 0:
                ans = 1
                for j in range(len(nums)):
                    if j != i:
                        ans *= nums[j]
                tab[i] = ans
                return tab
            tab[i] = tab[i] // nums[i]
        return tab