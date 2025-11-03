class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        colors = list(colors)
        ans = neededTime[0]
        left= 0
        tempsum = 0

        while left+1<=len(colors)-1:
            # left0 = left - 1

            if left+1<=len(colors)-1 and colors[left] == colors[left+1]:
        
                while colors[left] == colors[left+1]:
                    
                    
                    left+=1
                    ans+=neededTime[left]
                    if not left+1<=len(colors)-1:
                        break
                            


            
            left+=1
            ans+=neededTime[left]
        return ans
solution = Solution()
print(solution.minCost("bbbaaa",[4,9,3,8,8,9]))