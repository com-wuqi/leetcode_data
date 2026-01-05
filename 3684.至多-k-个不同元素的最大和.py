#
# @lc app=leetcode.cn id=3684 lang=python3
#
# [3684] 至多 K 个不同元素的最大和
#

from typing import List
# @lc code=start
class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        # python3 set() 可以将list 转化为集合, 并去重
        return sorted(set(nums),reverse=True)[:k]
# @lc code=end

