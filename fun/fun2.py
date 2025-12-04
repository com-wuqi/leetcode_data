class Solution:
    def solve(self, nums: list[int], k: int):
        nums.sort(reverse=True) 
        # 从大到小排序
        delt = sum(nums) % k
        if delt == 0:
            return 0
        ans = 0
        for i in nums:
            delt -= i
            ans += 1
            if delt <= 0:
                break
        return ans


slu = Solution()
test1 = slu.solve([2,2,2],7) 

print(test1)
