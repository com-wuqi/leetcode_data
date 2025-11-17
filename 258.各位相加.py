#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        self.ans=0
        def dfs(i:int) -> int:
            if i<10:
                self.ans=i
                return
            str1=str(i)
            t=0
            for m in str1:
                t+=int(m)
            dfs(t)
        dfs(num)
        return self.ans
    
# 见 test258
# 直接覆盖需要nonlocal修饰
# @lc code=end

