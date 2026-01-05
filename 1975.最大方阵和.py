#
# @lc app=leetcode.cn id=1975 lang=python3
#
# [1975] 最大方阵和
#

from typing import List
# @lc code=start
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # 思路的复刻
        list_1 = [] # 负数
        ans = 0
        is_find0 = False
        min_int = float("inf") # 大于0最小的
        for j in matrix:
            for i in j:
                if i > 0 :
                    ans+=i
                    min_int = min(i,min_int)
                elif i < 0:
                    list_1.append(i)
                else:
                    is_find0 = True

        if len(list_1)%2==0 or is_find0:
            # 偶数，或者存在 0 
            ans+=sum([abs(t) for t in list_1])
        else:
            mxn_1 = max(list_1) # 负数中最大的
            if abs(mxn_1) < abs(min_int):
                for k in list_1:
                    if k == mxn_1:
                        ans+=k
                        mxn_1 = 1
                    else:
                        ans+=-k
            else:
                ans+=sum([abs(t) for t in list_1])
                ans-=2*min_int


        return ans

# @lc code=end

