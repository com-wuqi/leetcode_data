#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

from typing import List


# @lc code=start
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # 思路复刻
        a, b = 0, 1  # 偶数位，奇数位
        while a < len(nums) and b < len(nums):
            if nums[a] % 2 == 0:
                a += 2
            elif nums[b] % 2 == 1:
                b += 2
            else:
                nums[a], nums[b] = nums[b], nums[a]
                a += 2
                b += 2
                # 互换后移动，防止死循环
        return nums


# @lc code=end
