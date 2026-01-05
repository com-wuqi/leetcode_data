#
# @lc app=leetcode.cn id=2273 lang=python3
#
# [2273] 移除字母异位词后的结果数组
#

from typing import List
# @lc code=start
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        size = 1
        for i in range(1,len(words)):
            if sorted(words[i]) != sorted(words[size-1]):
                words[size] = words[i]
                size+=1

        return words[:size]
# @lc code=end

