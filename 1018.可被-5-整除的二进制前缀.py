#
# @lc app=leetcode.cn id=1018 lang=python3
#
# [1018] 可被 5 整除的二进制前缀
#

from typing import List
# @lc code=start
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = [False,]*len(nums)
        array = ''
        for i in range(len(nums)):
            array+=str(nums[i])
            if int(array,2) % 5==0:
                ans[i]=True
        return ans
# @lc code=end

