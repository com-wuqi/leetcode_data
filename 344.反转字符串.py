#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left=0 # 左指针
        right=len(s)-1 # 右指针
        while left<right:
            s[left],s[right] = s[right],s[left]
            left+=1
            right-=1
        """
        换一种写法, 更加像之前写的双指针?
        打住. 不行, 因为右指针顺序反了
        """
        


# @lc code=end

