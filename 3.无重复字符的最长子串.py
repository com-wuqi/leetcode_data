#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        result = [
            1,
        ]
        for left in range(len(s) - 1):
            templist = []
            right = left + 1
            if s[left] != s[right]:
                templist.append(s[left])
                templist.append(s[right])
                if right < len(s)-1:
                    while right < len(s) - 1:
                        right += 1
                        if s[right] not in templist:
                            templist.append(s[right])
                        else:
                            result.append(len(templist))
                            break
                    result.append(len(templist))
                else:
                    result.append(len(templist))
        return max(result)





# @lc code=end

