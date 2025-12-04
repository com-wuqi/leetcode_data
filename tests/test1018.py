from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = [False,]*len(nums)
        array = ''
        for i in range(len(nums)):
            array+=str(nums[i])
            if int(array,2) % 5==0:
                ans[i]=True
        return ans
    
slu = Solution()
test1 = slu.prefixesDivBy5([0,1,1,1,1,1])