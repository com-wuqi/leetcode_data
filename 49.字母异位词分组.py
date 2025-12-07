#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        v1 = defaultdict(list)
        for string in strs:
            sorted_str = "".join(sorted(string))
            v1[sorted_str].append(string)
        return list(v1.values())
            
# @lc code=end
    

