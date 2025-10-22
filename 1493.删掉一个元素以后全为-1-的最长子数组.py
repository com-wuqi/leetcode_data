#
# @lc app=leetcode.cn id=1493 lang=python3
#
# [1493] 删掉一个元素以后全为 1 的最长子数组
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        counts=0
        templist = []
        ans = 0
        for i in nums:
            if len(templist) == 0 and i == 0:
                continue

            templist.append(i)
            if i == 1:
                if counts == 0:
                    ans = max(ans,len(templist))
                else:
                    ans = max(ans,len(templist)-1)
            if i == 0 and counts==0:
                counts+=1

            if i == 0 and counts==2:
                # 临界
                templist=templist[templist.index(0)+1:]
                counts-=1
        return ans


# @lc code=end

