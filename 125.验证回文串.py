#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        isalnum()方法用于检测字符串是否只由字母和数字组成
        vscode代码提示原文:
        () -> bool
        Return True if the string is an alpha-numeric string, False otherwise.
        A string is alpha-numeric if all characters in the string are alpha-numeric 
        and there is at least one character in the string.
        """
        left=0
        right=len(s)-1
        while left<right:
            while left<=len(s)-1 and not s[left].isalnum():
                left+=1
            while right>=0 and not s[right].isalnum():
                right-=1
            if left<right:
                # 根据示例, 我们需要全部转换为小写字母
                if s[left].lower() == s[right].lower():
                    pass
                else:
                    return False
                left+=1
                right-=1
        return True

        
# @lc code=end

