#
# @lc app=leetcode.cn id=1574 lang=python3
#
# [1574] 删除最短的子数组使剩余数组有序
#

from typing import List


# @lc code=start
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

        ans = 0
        left = 0
        right = len(arr) - 1

        while right != 0 and arr[right] >= arr[right - 1]:
            right -= 1

        if right == 0:  # arr 已经是非递减数组
            return 0

        ans = right  # 有可能是最右边的一段，返回删除的值

        while left == 0 or arr[left] >= arr[left - 1]:

            # 左端点不小于右端点
            while right < len(arr) and not (arr[left] <= arr[right]):
                right += 1

            # 左端点小于右端点 + 左端点不小于右端点
            ans = min(ans, right - left - 1) 
            # 这里是递减的(left增且right不变时)
            
            left += 1
        return ans
    
# https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/solutions/2189149/dong-hua-yi-xie-jiu-cuo-liang-chong-xie-iijwz/

# @lc code=end
