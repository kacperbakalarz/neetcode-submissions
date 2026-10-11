class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        graph = [[] for _ in range(numCourses)]
        start = [0 for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        q = deque()
        for node in prerequisites:
            graph[node[1]].append(node[0])
            start[node[0]] += 1
        
        #print(start)

        for i in range(len(start)):
            if start[i] == 0:
                q.append(i)
                visited[i] = 1

        while q:
            node = q.popleft()
            visited[node] = 1
            for neighbour in graph[node]:
                new_city = neighbour
                start[new_city] -= 1
                if start[new_city] == 0:
                    q.append(new_city)
        #print(graph)
        #print(visited)
        if sum(visited) == numCourses:
            return True
        
        return False
                
        
        