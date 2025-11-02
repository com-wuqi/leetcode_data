#
# @lc app=leetcode.cn id=3643 lang=python3
#
# [3643] 垂直翻转子矩阵
#

# @lc code=start
class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        """
        整数 x 和 y 表示一个 正方形子矩阵 的左上角下标，整数 k 表示该正方形子矩阵的边长。
        """
        up = x # 首行
        down = x+k-1 # 尾行
        while up<down:
            grid[up][y:y+k],grid[down][y:y+k] = grid[down][y:y+k],grid[up][y:y+k]
            up+=1 # 下移
            down-=1 # 上移
        return grid

        
# @lc code=end

