#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        ans=0
        count0=0 # 计数器
        left=0
        for right,data in enumerate(nums):
            # 右端点参与遍历
            if data == 0:
                count0+=1
            while count0>k: 
                # 0 过多
                if nums[left] == 0:
                    count0-=1 
                    # 端点0移出时,维护计数器准确(窗口内现存的0的个数)
                left+=1
                # 移动左侧索引值
            ans = max(ans,right-left+1)
            # 窗口长度的最大值即为结果
        return ans

# @lc code=end

