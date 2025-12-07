#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#


from typing import List
# @lc code=start
class Solution:

    def lowerbound(self,nums:list,target:int):
        left = 0
        right = len(nums) - 1
        while left<=right:
            mid = (right+left) // 2
            if nums[mid] < target:
                left = mid +1
            else:
                right = mid-1
        return left
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.lowerbound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]  # nums 中没有 target
        # 如果 start 存在，那么 end 必定存在
        end = self.lowerbound(nums, target + 1) - 1
        return [start, end]


    

# @lc code=end

