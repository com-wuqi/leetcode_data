class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        ans = 0
        while left<right:
            # temp = 
            if nums[left] + nums[right] < lower:
                left+=1
                continue

            if nums[left] + nums[right] > upper:
                right-=1
                continue

            ans+=1
            print(f"{left} {right}")

            tempright = right
            while tempright>left:
                
                tempright-=1
                if nums[left] + nums[tempright] < lower or left>=tempright:
                    break
                ans+=1
                print(f"{left} {tempright}")
            
            left+=1
            
        return ans

"""
Time Limit Exceeded
50/55 cases passed (N/A)
Testcase
[33474,3048,55017,6445,836...]
Expected Answer:
4999950000
"""
slu = Solution()
print(slu.countFairPairs([0,1,7,4,4,5],3,6))
