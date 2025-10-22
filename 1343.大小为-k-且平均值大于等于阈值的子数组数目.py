#
# @lc app=leetcode.cn id=1343 lang=python3
#
# [1343] 大小为 K 且平均值大于等于阈值的子数组数目
#

# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        answer = 0
        nums = 0
        for index,data in enumerate(arr):
            nums += data
            if index -k + 1 < 0:
                continue
            if nums/k >=threshold:
                answer+=1
            nums -= arr[index -k +1]
        return answer
# @lc code=end

