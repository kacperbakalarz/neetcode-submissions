class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            parents = []
            for i in range(numCourses):
                parents.append(i)
            return parents

        graph = [[] for _ in range(numCourses)]
        start = [0 for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        parents = []
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
            parents.append(node)
            visited[node] = 1
            for neighbour in graph[node]:
                new_city = neighbour
                start[new_city] -= 1
                if start[new_city] == 0:
                    q.append(new_city)
        #print(graph)
        #print(visited)
        #print(sum(visited))
        #print(numCourses)
        #print(parents)
        if sum(visited) == numCourses:
           return parents
        
        return []
                