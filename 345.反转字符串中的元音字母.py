#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left=0
        right=len(s)-1
        while left<right:
            while left<=len(s)-1 and s[left] not in "aeiouAEIOU":
                # 同下
                left+=1
            while right>=0 and s[right] not in "aeiouAEIOU":
                """
                此处. 也可以写为 right>0 , 极限情况下 right=lrft
                没必要换
                """
                right-=1
            if left<right: 
                """
                这里 <= 和 < 均可, 其实等于时没必要换
                """
                s[left],s[right] = s[right],s[left]
                left+=1
                right-=1
                # 交换完记得再维护指针
        return "".join(s) # 拼接回去
# @lc code=end

