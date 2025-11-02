#
# @lc app=leetcode.cn id=1750 lang=python3
#
# [1750] 删除字符串两端相同字符后的最短长度
#

# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        """
        test1750.py (官方解法),效率更优
        """
        s=list(s)
        left = 0
        right = len(s)-1
        while left<right:
            if s[left]!=s[right]:
                break
            while left+1<=len(s)-1 and s[left] == s[left+1]:
                left+=1
            while right-1>=0 and s[right] == s[right-1]:
                right-=1
            s = s[left+1:right]
            left=0
            right=len(s)-1
            # 恢复索引
        return len(s)
# @lc code=end

