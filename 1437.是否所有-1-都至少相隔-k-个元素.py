#
# @lc app=leetcode.cn id=1437 lang=python3
#
# [1437] 是否所有 1 都至少相隔 k 个元素
#

from math import inf # 无穷
# @lc code=start
class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        last=-inf # 负无穷
        for i,d in enumerate(nums):
            if d != 1:
                continue
            if i-last-1<k:
                return False
            last=i
        return True

# @lc code=end

