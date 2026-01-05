from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = 0
        for i in nums:
            if i !=0 :
                nums[size] = i
                size+=1
        
        nums[size:] = [0,]*(len(nums)-(size-1)-1)
        # return nums
    
    def moveZeroes2(self,nums: List[int]) -> None:
        v0 = 0 # 标记换后的下一位
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[v0],nums[i] = nums[i],nums[v0]
                v0+=1
        return nums

slu = Solution()
test1 = slu.moveZeroes2([0,1,0,3,12])
print(test1)

