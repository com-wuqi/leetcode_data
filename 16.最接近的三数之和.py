#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

from math import inf


# @lc code=start
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        lenth = len(nums)
        delt = +inf
        ans = 0
        for i in range(len(nums) - 2):
            # 枚举到倒数第二个元素
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = lenth - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp == target:
                    return target

                if abs(temp - target) < delt and (temp - target) > 0:
                    delt = min(delt, abs(temp - target))
                    ans = temp
                    right -= 1
                elif (temp - target) > 0:
                    right -= 1

                if abs(temp - target) < delt and (temp - target) < 0:
                    delt = min(delt, abs(temp - target))
                    ans = temp
                    left += 1
                elif (temp - target) < 0:
                    left += 1

        return ans


# @lc code=end
