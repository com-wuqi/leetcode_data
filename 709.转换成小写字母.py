#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] 转换成小写字母
#

# @lc code=start
class Solution:
    def toLowerCase(self, s: str) -> str:
        ans=[]
        for i in s:
            ans.append(str.lower(i))
        return "".join(ans)
# @lc code=end

