#
# @lc app=leetcode.cn id=2962 lang=python3
#
# [2962] 统计最大元素出现至少 K 次的子数组
#

from collections import defaultdict

# @lc code=start
class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        cnts = 0
        ans = left = 0
        mx = max(nums)
        for data in nums:
            if data == mx:
                cnts+=1
            while cnts>=k: 
                # 将左侧索引从 left 移动为 left-1
                if nums[left]==mx:
                    cnts-=1
                left+=1
            ans+=left
        return ans


# @lc code=end

