#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if target>sum(nums):
            # 不存在答案
            return 0
        sums=0
        left=0
        ans=len(nums)+1 # 取最小值的话, ans初始化为最大情况
        for right,data in enumerate(nums):
            sums+=data
            while sums>=target:
                # 条件成立, 开始移动左端点
                ans = min(ans,right-left+1)
                sums-=nums[left]
                left+=1
        return ans


# @lc code=end

