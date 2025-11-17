#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        ans=0
        for i,d in enumerate(nums):
            for j in nums[i+1:]:
                if d==j:
                    ans+=1
        return ans
# @lc code=end

