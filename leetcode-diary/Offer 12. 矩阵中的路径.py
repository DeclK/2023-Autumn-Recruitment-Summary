from ctypes.wintypes import WORD
from re import search
from typing import List
from unittest import result


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 深度搜索
        m = len(board)
        n = len(board[0])
        def is_valid(i, j):
            if 0 <= i < m and 0 <= j < n:
                return True
            return False
        def dfs(i, j, status, target):
            if board[i][j] == word[target]:
                if target == len(word) - 1:
                    return True
                search_list = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
                status[i][j] = 1
                for i_ , j_ in search_list:
                    if is_valid(i_, j_) and status[i_][j_] == 0:
                        if dfs(i_ , j_, status, target + 1):
                            return True
                status[i][j] = 0
                return False
            return False
        status = [[0] * n for j in range(m)]
        for i in range(m):
            for j in range(n):
                if dfs(i, j, status, 0):
                    return True
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
# board = [["a","b"],["c","d"]]
# word = "cdba"
# board = [["a","a"]]
# word = 'aaa'
# board = [["C","A","A"],["A","A","A"],["B","C","D"]]
# word = "AAB"
test = Solution()
print(test.exist(board, word))
