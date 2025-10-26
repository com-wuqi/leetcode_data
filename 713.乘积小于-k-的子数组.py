#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于 K 的子数组
#


# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            # 0 <= k <= 10^6
            return 0
        ans = left = 0
        counts = 1
        for right, data in enumerate(nums):
            counts *= data
            while counts >= k: #严格小于, 所以是大于等于
                counts /= nums[left]
                left += 1
            ans += right - left + 1
        return ans


# @lc code=end
