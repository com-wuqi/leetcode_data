from collections import defaultdict


# dict1 = defaultdict(list)
# dict1["a"] = [12,34]
# print(len(dict1))


# for i in dict1:
#     print(i)

l1 = [0,1,2]

for i in range(2,len(l1)-1):
    print(l1[i-2:i+1])
    k = l1[i]
    i = l1[i-2]
    print(2*(k-i))


class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        if len(nums)<3:
            return -1
        dict1 = defaultdict(list)
        ans = float('inf')
        for index,data in enumerate(nums):
            dict1[data].append(index)
        
        for i in dict1:
            if len(dict1[i]) < 3:
                continue

            print(dict1[i])
            for j in range(2,len(dict1[i])):


                # t1 = dict1[i][j]
                # t2 = dict1[i][j-2]
                ans = min(ans,2*(dict1[i][j]-dict1[i][j-2]))
        return ans

solution = Solution()
print(solution.minimumDistance([1,2,1,1,3]))

# 显然, 我们需要取连续的三个元素
# dict1.values() 一定是排序完成的(从小到大)
# abs(i - j) + abs(j - k) + abs(k - i)
# = j - i + k -j +k - i 
# = 2(k-i)
# float("inf") 是无穷大