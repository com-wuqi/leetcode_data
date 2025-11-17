class Solution:
    def addDigits(self, num: int) -> int:
        def dfs(i: int) -> int:
            if i < 10:
                return i
            
            str1 = str(i)
            t = 0
            for m in str1:
                t += int(m)
            return dfs(t)  # 添加 return
        return dfs(num)
slu=Solution()
test1=slu.addDigits(38)
print(test1)