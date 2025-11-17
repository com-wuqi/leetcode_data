class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        list1=[]
        for i in range(len(nums)):
            if nums[i]==1:
                list1.append(i)
            if len(list1)<2:
                continue
            if list1[-1]-list1[-2]-1<k:
                return False
            del list1[0]
        return True

# class Solution:
#     def kLengthApart(self, nums: list[int], k: int) -> bool:
#         list1=[]
#         for i in range(len(nums)):
#             if nums[i]==1:
#                 list1.append(i)
#         for j in range(1,len(list1)):
#             if list1[j]-list1[j-1]-1<k:
#                 return False
#         return True

slu=Solution()
test1=slu.kLengthApart([1,0,0,0,1,0,0,1],2)
print(test1)