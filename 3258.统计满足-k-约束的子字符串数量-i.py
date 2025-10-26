#
# @lc app=leetcode.cn id=3258 lang=python3
#
# [3258] 统计满足 K 约束的子字符串数量 I
#


# @lc code=start
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        """
        内层循环结束后，[left,right] 这个子数组是满足题目要求的。
        由于子数组越短，越能满足题目要求，所以除了 [left,right],
        还有 [left+1,right],[left+2,right],…,[right,right] 都是满足要求的。
        也就是说，当右端点固定在 right 时，
        左端点在 left,left+1,left+2,…,right 的所有子数组都是满足要求的，
        这一共有 right-left+1 个。

        """
        ans = 0
        counts = [0,0] # 统计0和1的个数
        left = 0
        for right,data in enumerate(s):
            counts[int(data)]+=1
            while (counts[0] >k and counts[1]>k):
                counts[int(s[left])]-=1
                left+=1
            # 越小越合法, 所以不需要 if 
            ans+=right-left+1
        return ans


# @lc code=end
