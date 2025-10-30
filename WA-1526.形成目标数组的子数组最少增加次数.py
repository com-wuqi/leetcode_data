#
# @lc app=leetcode.cn id=1526 lang=python3
#
# [1526] 形成目标数组的子数组最少增加次数
#

# @lc code=start
class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        if target[0] == target[-1]:
            return max(target)
        sign = 0 # 标记特殊情况
        if target[0] == max(target):
            side = target[0]  
            del target[0]
            sign = 1
        elif target[-1] == max(target):
            side = target[-1]
            del target[-1]
            sign = 1
        elif target[0] > target[-1]:
            side = target[0]
            del target[0]
        elif target[0] < target[-1]:
            side = target[-1]
            del target[-1]
        p1 = target[0]-target[-1]
        ans = side if sign == 0 else 0 # 理想情况
        tempans = 0
        for data in target:
            temp = data-side
            if temp == p1 or temp==-p1 or temp==0:
                continue
            else:
                if temp>0:
                    tempans+=temp
                elif temp<0:
                    tempans+=-temp
        ans+=tempans if tempans !=0 else max(target)
        return ans
                
        
                
        
# @lc code=end

