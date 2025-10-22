#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#


# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        counts, answer = 0, 0
        for index, data in enumerate(s):
            if data in "aeiou":
                counts += 1
            if index - k + 1 < 0:
                continue  # 边界不存在, 让for再移动
            answer = max(counts, answer)
            if s[index - k + 1] in "aeiou":
                counts -= 1
            # 如果边界在下一次循环前符合条件,那么需要将计数器减一
            # 第一个if判断移动后进入的字符是否符合要求
            # 最后一个判断即将离开边界的是否符合要求
        return answer


# @lc code=end
