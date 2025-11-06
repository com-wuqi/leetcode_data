#
# @lc app=leetcode.cn id=1658 lang=python3
#
# [1658] 将 x 减到 0 的最小操作数
#


# @lc code=start
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        # 借鉴的思路: x + 窗口内值 = sum_nums
        # 是啊, 为什么不能换个方向解决问题
        ans = -1  # 此处的ans不是目标长度, 而是窗口长度
        sum_nums = sum(nums)
        sums, left = 0, 0
        for right, data in enumerate(nums):
            sums += data
            if sums + x == sum_nums:
                ans = max(ans, (right - left + 1))

            while sums + x > sum_nums and left <= right:
                # left <= right 防一手indexError
                # 补充: 因为过大所以移动 left 来缩小使其相等有风险
                # , 1 <= nums[i] 才行, 若 nums[i]<=0 , 考虑 前缀和
                sums -= nums[left]
                left += 1
            if sums + x == sum_nums:
                ans = max(ans, (right - left + 1))
        if ans == -1:
            # 没找到答案
            return ans
        else:
            return len(nums) - ans


# @lc code=end
