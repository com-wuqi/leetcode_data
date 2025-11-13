#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        maps = ("","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz")
        # maps[0] ... 一一对应
        # digits>=1
        lenth = len(digits)
        ans = []
        path = ["",]*lenth
        # path 对应每一种可能, 长度是lenth
        def dfs(i):
            if i == lenth:
                ans.append("".join(path))
                # 边界, i 是 digits[0] 到 digits[i-1] 的所有可能
                return
            for c in maps[int(digits[i])]:
                path[i] = c
                dfs(i+1)
                # 这里 dfs(i+1) 有 3 条世界线
                # 分别对应 maps[int(digits[i])] 的三个元素
        
        dfs(0) # 从 digits[0] 开始
        return ans
# 
# @lc code=end

