class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        dq = deque()
        ans =[]
        for i in range(len(nums)):
            num = nums[i]
            if dq and dq[0] == i-k:
                dq.popleft()
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            
            dq.append(i)

            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans