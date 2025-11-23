from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # 问题是：1<=a<=b<=c and a+b > c
        # 考虑优化

        nums.sort()
        ans = 0
        for indxC in range(2,len(nums)):
            c = nums[indxC]
            if not(nums[indxC-1] + nums[indxC-2] > c):
                # fix1: 
                # 当前c比最大的a+b还要大(a+b<=c)，过大
                # 虽然c递增，但是无法判断后续c的情况
                # 已知 [a,b,c,d] (d>c) (a+b<=c)
                # 不知 d-c 和 a 的大小关系，不确定
                continue

            left = 0
            right = indxC -1
            while left<right:
                # [[left],...,[right],[indxC]]
                a = nums[left]
                b = nums[right]
                if a+b>c:
                    # 这里存在答案
                    # nums[left] 到 nums[right-1] 一定都合法
                    ans+=right-left
                    # b = nums[right] 全部考虑完啦
                    right-=1
                else:
                    # 在 b = nums[right] 下，和仍然太小
                    left+=1
        return ans
    def triangleNumber_2(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        # 这个优化需要倒序 c 的位置
        for idxC in range(len(nums)-1,1,-1):
            # 左端点: len(nums)-1 (因为能取到)
            # 右端点: 1+1=2 (因为取不到)
            c = nums[idxC]
            if not(nums[idxC-1] + nums[idxC-2] > c):
                continue

            if nums[0]+nums[1]>c:
                # c 已经是最小值了，再次右移动一定没有
                # 当前c下，整个区间任取3个数均可
                # ans+=c(idx+1)(3)
                ans+=(idxC+1)(idxC)(idxC-1)/6
                break # 再次右移动一定没有

            left = 0
            right = idxC - 1
            while left<right:
                a = nums[left]
                b = nums[right]
                if a+b>c:
                    ans+=right-left
                    # 当前 right 下所有成立的值都已经统计
                    right-=1
                else:
                    left+=1
        return ans


