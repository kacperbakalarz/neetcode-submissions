class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        max_heap = [-n for n in stones]  
        heapq.heapify(max_heap)     
        while len(max_heap) >= 2:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            heapq.heappush(max_heap,-abs(first-second))
        return -max_heap[0]