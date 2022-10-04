from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, graph, target):
            if i == n or i < 0: return False
            if j == m or j < 0: return False
            if graph[i][j] == 1: return False
            s = board[i][j]
            if s != word[target]:
                return False
            if target == len(word) - 1:
                return True
            graph[i][j] = 1
            search = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
            flag = False
            for i_, j_ in search:
                flag = flag or dfs(i_, j_, graph, target + 1)
                if flag:
                    graph[i][j] = 0
                    return True
            graph[i][j] = 0
            return flag
        n = len(board)
        m = len(board[0])
        graph = [[0] * m for _ in range(n)]
        flag = False
        for i in range(n):
            for j in range(m):
                flag = flag or dfs(i, j, graph, 0)
                if flag: return True
        return False

        
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]; word = "ABCCEE"
test = Solution()
print(test.exist(board, word))