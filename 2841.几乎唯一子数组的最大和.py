#
# @lc app=leetcode.cn id=2841 lang=python3
#
# [2841] 几乎唯一子数组的最大和
#

# @lc code=start
class Solution:
    def maxSum(self, nums: list[int], m: int, k: int) -> int:
        ans = 0
        sums = []
        counts = 0
        for index,data in enumerate(nums):
            if data not in sums:
                sums.append(data)
                counts+=1
            elif data in sums:
                sums.append(data)
            
            if index -k + 1 <0:
                continue
            if counts >= m:
                ans = max(ans,sum(sums))
            
            tempstr = sums[0]
            del sums[0]
            if tempstr not in sums:
                # 去除了一个唯一存在的元素
                counts-=1
        return ans
# @lc code=end

