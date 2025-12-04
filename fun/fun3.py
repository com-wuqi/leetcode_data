class Solution:
    def solve(self, nums: list[int], k: int):
        a=sum(nums)%k
        if a==0:
            return 0
        nums.sort()
        size=len(nums)
        b=1
        for i in range(size-1):
            if nums[size-1-i]>=a:
                return b
            else:
                b+=1
                nums[size-2-i]+=nums[size-1-i]


slu = Solution()
test1 = slu.solve([2,2,2],7) 

print(test1)