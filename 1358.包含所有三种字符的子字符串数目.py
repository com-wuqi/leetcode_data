#
# @lc app=leetcode.cn id=1358 lang=python3
#
# [1358] 包含所有三种字符的子字符串数目
#

from collections import defaultdict


# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans, left = 0, 0
        cnts = defaultdict(int)
        for _, data in enumerate(s):
            cnts[data] += 1
            while len(cnts) == 3:  # 3个字母都存在的时候
                cnts[s[left]] -= 1
                if cnts[s[left]] == 0:
                    del cnts[s[left]]
                left += 1
            ans += left
        return ans


# @lc code=end
