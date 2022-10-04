from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)  # m 行
        n = len(board[0])   # n 列
        # status = [[0 for i in range(n)] for j in range(m)]
        ship_num = 0
        def search(i, j):
            # 搜索四周的 X 并返回其数字
            num = 0
            search_list = [(i - 1, j), (i + 1, j), (i , j - 1), (i, j + 1)]
            for i, j in search_list:
                if 0 <= i < m and 0 <= j < n:
                    if isinstance(board[i][j], int):
                        num = board[i][j]
                        break
            return num
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    # 搜索附近是否存在
                    num = search(i, j)
                    if num == 0:
                        ship_num += 1
                        board[i][j] = ship_num
                    else:
                        board[i][j] = num
        return ship_num


test = Solution()
board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
print(test.countBattleships(board))