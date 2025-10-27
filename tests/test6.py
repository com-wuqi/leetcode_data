from collections import defaultdict

from collections import defaultdict

class Solution:
    def maxConsecutiveAnswersPlus(self, answerKey: str, k: int) -> int:
        counts = defaultdict(int)
        left = 0
        ans = 0
        
        for right in range(len(answerKey)):
            counts[answerKey[right]] += 1
            
            # 每次重新计算当前窗口内的最大出现次数
            max_count = max(counts.values())
            
            # 如果窗口长度减去最大出现次数 > k，说明需要缩小窗口
            while (right - left + 1) - max_count > k:
                counts[answerKey[left]] -= 1
                left += 1
                # 缩小窗口后重新计算最大出现次数
                max_count = max(counts.values())
            
            ans = max(ans, right - left + 1)
        
        return ans
    
solution = Solution()
# 测试样例1
print(solution.maxConsecutiveAnswersPlus("AABB", 2))  # 预期输出: 4

# 测试样例2  
print(solution.maxConsecutiveAnswersPlus("ABCC", 1))  # 预期输出: 3

# 测试样例3
print(solution.maxConsecutiveAnswersPlus("AACACCBBAAC", 2))  # 预期输出: 5

# 测试样例4
print(solution.maxConsecutiveAnswersPlus("ABCD", 3))  # 预期输出: 4

# 测试样例5
print(solution.maxConsecutiveAnswersPlus("AAAA", 0))  # 预期输出: 4