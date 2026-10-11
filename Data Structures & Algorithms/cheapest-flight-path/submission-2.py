import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for node in flights:
            graph[node[0]].append((node[1],node[2]))
        costs = [[float('inf')]*(k+2) for _ in range(n)]
        costs[src][0] = 0
        queue = []
        heapq.heapify(queue)
        heapq.heappush(queue,(0,src,0))
        
        while len(queue) > 0 :
            cost,city,stops = heapq.heappop(queue)
            if city == dst:
                return cost
            if cost > costs[city][stops]:
                continue
            for neighbour in graph[city]:
                new_city = neighbour[0]
                new_cost = cost + neighbour[1]
                #new_stops = stops + 1
                if stops <= k:
                    if new_cost <= costs[new_city][stops+1]:
                        costs[new_city][stops+1] = new_cost
                        heapq.heappush(queue,(new_cost,new_city,stops+1))
        return -1 
        #print(costs)


            
            


       
