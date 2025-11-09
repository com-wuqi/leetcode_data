#
# @lc app=leetcode.cn id=3740 lang=python3
#
# [3740] 三个相等元素之间的最小距离 I
#

from collections import defaultdict
# @lc code=start
class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        if len(nums)<3:
            return -1
        dict1 = defaultdict(list)
        ans = float("inf")
        for index,data in enumerate(nums):
            dict1[data].append(index)
        
        for i in dict1:
            if len(dict1[i]) < 3:
                continue
            for j in range(2,len(dict1[i])):
                # 显然, 我们需要取连续的三个元素,这样可能距离最小
                # dict1.values() 一定是排序完成的(从小到大)
                # 见 test3740.py
                ans = min(ans,2*(dict1[i][j]-dict1[i][j-2]))
        return ans if ans!=float("inf") else -1

# @lc code=end

