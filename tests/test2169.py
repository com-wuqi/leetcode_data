class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while(num2!=0 and num1!=0):
            if num2>num1:
                num2-=num1
            else:
                num1-=num2
            ans+=1
        return ans

solution = Solution()
print(solution.countOperations(2,3))