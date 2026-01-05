#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#

from typing import List
# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # 与 test283 第二种解法类似
        sign = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                # 如果是偶数，互换
                nums[sign],nums[i] = nums[i],nums[sign]
                sign+=1
        return nums
# @lc code=end

