from typing import List
# @lc code=start
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # 思路复刻
        a,b = 0,1 # 偶数位，奇数位
        while 1:
            while nums[a] % 2 == 0 :
                a+=2
                if a>=len(nums):
                    break
            while nums[b] % 2 == 1:
                b+=2
                if b>=len(nums):
                    break
            if a>=len(nums) or b>=len(nums):
                break
            else:
                # 互换
                nums[a],nums[b] = nums[b],nums[a]
            
        return nums
    
# 另一种循环
