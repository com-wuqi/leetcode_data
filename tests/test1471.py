class Solution:
    def getStrongest(self, arr: list[int], k: int) -> list[int]:
        arr.sort()
        mid = arr[int((len(arr)-1)/2)]
        left = 0
        right = len(arr)-1
        ans = [0]*k
        for i in range(k):

            if abs(arr[left]-mid) > abs(arr[right]-mid):
                ans[i] = arr[left]
                left+=1
            else:
                ans[i] = arr[right]
                right-=1
        
        return ans

solution = Solution()
print(solution.getStrongest([-7,22,17,3],2))