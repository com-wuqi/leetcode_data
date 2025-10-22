#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        minlenth=201
        for i in strs:
            if len(i)<minlenth:
                minlenth = len(i)
        
# @lc code=end

