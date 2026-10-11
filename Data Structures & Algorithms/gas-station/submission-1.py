class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        curr = 0 
        visited = [0 for _ in range(len(gas))]
        ans = 0
        for i in range(len(gas)):
            curr += gas[i]-cost[i]
            if curr < 0:
                ans = i+1
                curr = 0
        return ans