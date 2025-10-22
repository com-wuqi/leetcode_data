class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        minlenth = len(s) + 1
        sums = 0
        ans = ""
        left = 0
        ansindex = len(s)
        for right, data in enumerate(s):
            sums += int(data)
            if sums == k:
                if (right - left + 1 < minlenth) or ( right - left + 1 == minlenth and left < ansindex):

                    ansindex = left
                    minlenth = right - left + 1
                    ans = s[left : right + 1]

            while (sums > k or int(s[left])==0) and left<right:
                sums -= int(s[left])
                left += 1
                if sums == k:
                    if (right - left + 1 < minlenth) or ( right - left + 1 == minlenth and left < ansindex):
                        ansindex = left
                        minlenth = left - right + 1
                        ans = s[left : right + 1]

        return ans

solution = Solution
test1 = solution.shortestBeautifulSubstring(solution,"1100001110111100100",8)
print(test1)