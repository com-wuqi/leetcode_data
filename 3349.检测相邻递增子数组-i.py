#
# @lc app=leetcode.cn id=3349 lang=python3
#
# [3349] 检测相邻递增子数组 I
#


# @lc code=start
class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        if k == 1:
            return True

        templist = []
        indexlist = []
        for index, data in enumerate(nums):
            if index == 0:
                templist.append(data)
                continue

            if data > templist[-1]:
                templist.append(data)
                if len(templist) == k:
                    indexlist.append(index)
                    del templist[0]
                else:
                    pass
            else:
                templist.append(data)
                templist = [
                    templist[-1],
                ]
        # print(indexlist)
        for i in indexlist:
            if i + k in indexlist:
                return True
        return False


# @lc code=end
