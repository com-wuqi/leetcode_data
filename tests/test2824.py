class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = 0
        while left < right:
            temp = nums[left] + nums[right]
            if temp >= target:
                right -= 1
                continue

            ans += right - left
            left += 1

        return ans


# 注意审题

slu = Solution()
print(slu.countPairs([-1, 1, 2, 3, 1], 2))
