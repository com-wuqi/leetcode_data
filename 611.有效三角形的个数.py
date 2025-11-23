#
# @lc app=leetcode.cn id=611 lang=python3
#
# [611] 有效三角形的个数
#

from typing import List
# @lc code=start

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # https://leetcode.cn/problems/valid-triangle-number/solutions/2432875/zhuan-huan-cheng-abcyong-xiang-xiang-shu-1ex3/
        # 问题是：1<=a<=b<=c and a+b > c

        nums.sort()
        ans = 0
        for indxC in range(2,len(nums)):
            c = nums[indxC]
            left = 0
            right = indxC -1
            while left<right:
                # [[left],...,[right],[indxC]]
                a = nums[left]
                b = nums[right]
                if a+b>c:
                    # 这里存在答案
                    # nums[left] 到 nums[right-1] 一定都合法
                    ans+=right-left
                    # b = nums[right] 全部考虑完啦
                    right-=1
                else:
                    # 在 b = nums[right] 下，和仍然太小
                    left+=1
        return ans


# @lc code=end

