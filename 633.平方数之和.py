#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

from math import sqrt


# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        l1 = [x for x in range(0, int(sqrt(c)) + 1)]
        # r2 = int(sqrt(c))-1 (手动测试可知)
        left, right = 0, len(l1) - 1
        while left < right:

            if l1[left] ** 2 + l1[right] ** 2 > c and left < right:
                right -= 1

            if l1[left] ** 2 + l1[right] ** 2 < c and left < right:
                left += 1
                # 注意,此处包含了 left==right 的情况

            if l1[left] ** 2 + l1[right] ** 2 == c:
                return True
        return False


# @lc code=end
