#
# @lc app=leetcode.cn id=2904 lang=python3
#
# [2904] 最短且字典序最小的美丽子字符串
#


# @lc code=start
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        """
        在Python中,
        我们可以直接使用比较运算符(如<, <=, >, >=, ==, !=)来比较两个字符串的字典序。
        """
        if s.count("1") < k:
            return ""
        ans = s
        counts = left = 0
        for right, data in enumerate(s):
            counts += int(data)
            while counts > k or int(s[left]) == 0:
                # 注意 counts!=k 这个结构里面没有合法的值
                counts -= int(s[left])
                left += 1
            if counts == k: # 判断后置
                temp = s[left : right + 1]
                if len(temp) < len(ans) or (len(temp) == len(ans) and temp < ans):
                    ans = temp
        return ans


# @lc code=end
