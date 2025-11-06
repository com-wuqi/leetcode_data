#
# @lc app=leetcode.cn id=1471 lang=python3
#
# [1471] 数组中的 k 个最强值
#


# @lc code=start
class Solution:
    def getStrongest(self, arr: list[int], k: int) -> list[int]:
        arr.sort()
        mid = arr[int((len(arr) - 1) / 2)]
        # mid 的计算极易写错
        left = 0
        right = len(arr) - 1
        ans = [0] * k
        for i in range(k):

            if abs(arr[left] - mid) > abs(arr[right] - mid):
                ans[i] = arr[left]
                left += 1
            # elif abs(arr[left] - mid) < abs(arr[right] - mid):
            #     ans[i] = arr[right]
            #     right -= 1
            # 与下面的情况处理的方式相同, 可以优化掉
            else: # abs(arr[left] - mid) == abs(arr[right] - mid)
                # 如果相等, arr[left]<0<arr[right]
                ans[i] = arr[right]
                right -= 1

        return ans


# @lc code=end
