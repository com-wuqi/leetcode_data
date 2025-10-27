# @lc code=start
from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans, left = 0, 0
        cnts = defaultdict(int)
        for _, data in enumerate(s):
            cnts[data] += 1
            while len(cnts) == 3:  # 3个字母都存在的时候
                cnts[s[left]] -= 1
                if cnts[s[left]] == 0:
                    del cnts[s[left]]
                left += 1
            ans += left
        return ans
solution = Solution()
print(solution.numberOfSubstrings("abcabc"))

"""
left=1 window=(a)bc anshave={abc} ans+=1
left=2 window=(b)ca anshave={bca,abca} ans+=2
left=3 window=(c)ab anshave={cab,bcab,abcab} ans+=3

"""