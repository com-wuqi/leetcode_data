#
# @lc app=leetcode.cn id=2024 lang=python3
#
# [2024] 考试的最大困扰度
#

from collections import defaultdict


# @lc code=start
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        counts = defaultdict(int) # 哈希表
        ans = 0
        left = 0
        for right, data in enumerate(answerKey):
            counts[data] += 1
            while counts["T"] > k and counts["F"] > k:
                # 无论翻转 T 还是 F 都无法确保窗口内字符相同
                counts[answerKey[left]] -= 1
                left += 1
                # 移动左端点, 维护哈希表
            ans = max(ans, right - left + 1)
            # 窗口最大长度即为 "最大化 的 连续相同 结果的题数"
        return ans


# @lc code=end
