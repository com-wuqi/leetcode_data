#
# @lc app=leetcode.cn id=2090 lang=python3
#
# [2090] 半径为 k 的子数组平均值
#


# @lc code=start
class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        # 易知, 固定窗口长度是 2k+1
        # 去除指定区域的 -1 即可
        d = 2 * k + 1
        if d > len(nums):  # 我总感觉没考虑全, 但是大样例测试没问题
            return [
                -1,
            ] * len(nums)
        ans = [
            -1,
        ] * len(nums)
        sums = 0
        for index, data in enumerate(nums):
            sums += data
            if index - d + 1 < 0:
                # 窗口长度不够
                continue
            # 注意读题, 是所有元素的平均值
            ans[index - k] = int(sums / d)
            # 题目要求截断(即去除小数)
            sums -= nums[index - d + 1]
        return ans


# @lc code=end
