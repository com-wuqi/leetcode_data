#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        path = []
        lenth = len(nums)
        # 不知道也没有必要预先定义 path 的长度
        def dfs(i):
            if i == lenth:
                ans.append(path.copy())
                # copy() 方法用于创建列表的浅拷贝，仅复制第一层元素
                return
            
            dfs(i+1)
            # 考虑不选该元素

            path.append(nums[i])
            dfs(i+1)
            # 考虑选这个元素

            path.pop(-1)
            # 恢复现场, 
            # 因为 dfs(i+1) 会再一次执行 dfs(), 使 不选择i元素 的情况增加元素
        dfs(0)
        return ans
"""
在Python中, 列表是引用类型。
当使用ans.append(path)时，
ans存储的是path的引用(即指向同一个列表对象)，而非独立副本。
在递归回溯过程中, path会被反复修改 (如path.pop()) ,
导致ans中所有子集最终都指向同一个被修改后的path

"""
# @lc code=end
