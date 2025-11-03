
class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        colors = list(colors)
        ans = 0
        left= 0

        while left+1<=len(colors)-1:
            # left0 = left - 1
            if colors[left] != colors[left+1]:
                left+=1
                continue
            if colors[left] == colors[left+1]:
                left0 = left
            if left+1<=len(colors)-1:
                while colors[left] == colors[left+1] and left+1<=len(colors)-1:

                    left+=1
                    if not left+1<=len(colors)-1:
                        break
                            
            print(neededTime[left0:left+2])

            ans+=sum(neededTime[left0:left+1])-max(neededTime[left0:left+1])

            left+=1
        return ans





solution = Solution()
print(solution.minCost("bbbaaa",[4,9,3,8,8,9]))