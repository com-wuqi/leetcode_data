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
            # 我们累加时间, 只需要去除消耗时间最长的那个元素
            # 对于 colors 的每个连续同色段，只能保留一个气球
            # 那么, 我们就不能去除最耗时的那个气球
            if neededTime[index] > tempmax:
                tempmax = neededTime[index]

            if index == len(colors)-1:
                # 此处是colors结束
                ans-=tempmax
                tempmax=0
                # 准备下一组max
                break
            if data != colors[index+1]:
                # 此处是连续相同颜色的结束点
                # 同时, 也是没有进入连续区间时, 恢复 ans 
                # (因为ans+=neededTime[index], neededTime[index] > tempmax = 0 恒成立,
                # 最后使 ans-==neededTime[index], ans=0
                ans-=tempmax
                tempmax=0
            

        return ans



# @lc code=end

