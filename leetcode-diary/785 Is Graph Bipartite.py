from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        status = [-1 for i in range(n)]
        ret = True
        def dfs(node, status):
            nonlocal ret
            for neighbor in graph[node]:
                if status[node]:
                    if status[neighbor] == 1:
                        return False
                    elif status[neighbor] == -1:
                        status[neighbor] = 0
                        ret = dfs(neighbor, status)
                else:
                    if status[neighbor] == 0:
                        return False
                    elif status[neighbor] == -1:
                        status[neighbor] = 1
                        ret = dfs(neighbor, status)
            return ret
        while -1 in status:
            node = status.index(-1)
            status[node] = 0
            ret = dfs(node, status) and ret
        return ret
    
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
test = Solution()
print(test.isBipartite(graph))