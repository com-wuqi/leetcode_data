#
# @lc app=leetcode.cn id=1578 lang=python3
#
# [1578] 使绳子变成彩色的最短时间
#

# @lc code=start
class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        ans = 0
        tempmax = 0
        for index,data in enumerate(colors):
            ans+=neededTime[index]
            if neededTime[index] > tempmax:
                tempmax = neededTime[index]

            if index == len(colors)-1:
                ans-=tempmax
                tempmax=0
                break
            if data != colors[index+1]:
                ans-=tempmax
                tempmax=0
            

        return ans



# @lc code=end

