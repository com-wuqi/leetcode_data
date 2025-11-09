from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l1 = [x for x in range(0, int(sqrt(c)) + 1)]
        # r2 = int(sqrt(c))-1 (手动测试可知)
        left, right = 0, len(l1)-1
        while left<right:
            
            if l1[left]**2 + l1[right]**2 > c and left<right:
                right-=1
            
            if l1[left]**2 + l1[right]**2 < c and left<right:
                
                left+=1

            if l1[left]**2 + l1[right]**2 == c:
                return True
        return False
    
slu = Solution()
print(slu.judgeSquareSum(4))