#
# @lc app=leetcode.cn id=2379 lang=python3
#
# [2379] 得到 K 个黑块的最少涂色次数
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        dict1 = {"W":0,"B":1}
        sums = 0
        maxsums = 0
        for index,data in enumerate(blocks):
            sums+=dict1[data]
            if sums == k:
                return 0
            if index - k + 1 <0:
                continue
            maxsums = max(maxsums,sums)
            if dict1[blocks[index -k +1]] == 1:
                sums -=1
        return k - maxsums

            

            
# @lc code=end

