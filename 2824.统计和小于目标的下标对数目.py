#
# @lc app=leetcode.cn id=2824 lang=python3
#
# [2824] 统计和小于目标的下标对数目
#


# @lc code=start
class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = 0
        while left < right:
            temp = nums[left] + nums[right]
            if temp >= target:
                right -= 1
                continue

            # temp<target
            ans += right - left
            # 当前答案存在, 即越短越合法(right到left+1)
            left += 1
            # 左端点为 left 的情况已经考虑完啦
        return ans


# @lc code=end
