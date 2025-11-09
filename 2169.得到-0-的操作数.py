#
# @lc app=leetcode.cn id=2169 lang=python3
#
# [2169] 得到 0 的操作数
#

# @lc code=start
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while(num2!=0 and num1!=0):
            if num2>num1:
                num2-=num1
            else:
                num1-=num2
            ans+=1
        return ans
# @lc code=end

