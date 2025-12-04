#
# @lc app=leetcode.cn id=948 lang=python3
#
# [948] 令牌放置
#

from typing import List
# @lc code=start
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l = 0
        r = len(tokens)-1
        temp = 0
        ans = 0
        while l<=r:
            if tokens[l]<=power:
                # 尽量换最便宜的
                temp+=1
                power-=tokens[l]
                l+=1
            elif tokens[l]>power and temp>0:
                # 有可能白换了：换完收益更低
                ans = max(ans,temp)
                temp-=1
                power+=tokens[r]
                r-=1
            else:
                break
        return max(ans,temp)


# @lc code=end

