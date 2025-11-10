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

            # ans+=1
            # print(f"{left} {right}")

            # tempright = right
            # while tempright>left:
                
            #     tempright-=1
            #     if nums[left] + nums[tempright] < lower or left>=tempright:
            #         break
            #     ans+=1
            #     # print(f"{left} {tempright}")

            ans+=right-left
            print(right-left)

            
            left+=1
            
        return ans

slu = Solution()
print(slu.countFairPairs([0,1,7,4,4,5],3,6))