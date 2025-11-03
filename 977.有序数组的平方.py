#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        lenth = len(nums)
        ans = [0,]*len(nums)
        left,right = 0,lenth-1
        insert = lenth-1 # 插入位置
        while insert>=0:
            v1 = nums[left]**2
            v2 = nums[right]**2
            if v1>v2:
                # 插入较大值
                ans[insert] = v1
                left+=1
            else:
                ans[insert] = v2
                right-=1
            insert-=1
        return ans
# @lc code=end

