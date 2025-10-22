from collections import defaultdict
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        counts = defaultdict(int) # 哈希表
        ans = 0
        left = 0
        window = ""
        for right, data in enumerate(answerKey):
            counts[data] += 1
            while counts["T"] > k and counts["F"] > k:
                window = answerKey[left:right+1]
                print(window)
                counts[answerKey[left]] -= 1
                left += 1
                window = answerKey[left:right+1]
                print(window)
            ans = max(ans, right - left + 1)
            window = answerKey[left:right+1]
            print(window)
        return ans

test1 = Solution.maxConsecutiveAnswers(Solution,"TTFTTFTT",1)
