import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #graph = []

        graph = [[] for _ in range(n)]
        for node in times:
            graph[node[0]-1].append((node[1]-1,node[2]))
        #print(graph)
        costs = [float('inf') for _ in range(len(graph))]
        costs[k-1] = 0
        queue = []
        heapq.heappush(queue,(0,k-1))
        while len(queue) > 0:
            cost,city = heapq.heappop(queue)
            if cost > costs[city]:
                continue
            for neighbour in graph[city]:
                new_cost = cost + neighbour[1]
                new_city = neighbour[0]
                if new_cost < costs[new_city]:
                    costs[new_city] = new_cost
                    heapq.heappush(queue,(new_cost,new_city))
        #print(costs)
        if max(costs) == float('inf'):
            return -1
        return max(costs)
