#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1 比特与 2 比特字符
#

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        # bits.pop()
        check=0
        i=0
        while i<len(bits)-1: # 判断到倒数第二位
            check+=1 if bits[i]==0 else 2
            # i 移动前检查
            i+=1 if bits[i]==0 else 2
            
        return check==len(bits)-1
# @lc code=end

