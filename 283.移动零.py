#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

from typing import List
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # size = 0
        # for i in nums:
        #     if i !=0 :
        #         nums[size] = i
        #         size+=1
        
        # nums[size:] = [0,]*(len(nums)-(size-1)-1)
        # # size-1 才是最后一位的索引

        v0 = 0 # 标记换后的下一位
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[v0],nums[i] = nums[i],nums[v0]
                v0+=1
        
        
        
# @lc code=end

