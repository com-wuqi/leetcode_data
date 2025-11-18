#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        尝试枚举nums[i], 对另外两个元素进行 两数之和II
        先排序, 再开始 相向双指针

        结构是这样的: [i]:枚举元素, [l]:左端点, [r]:右端点
        [[i],[l],...,[r]] 然后
        [...,[i],[l],...,[r]]
        每一次移动 [i], 都要重置 [l], [r] 的位置

        while l<r: 是根据 sums 的大小来移动 [l], [r]: 两者均向内移动
        [...,[i],...,[l],...,[r],...]
        然后 l+=1
        [...,[i],...,[l-1],[l],...,[r],...]
        while (l<r) and nums[l] == nums[l-1]:l+=1
        持续移动 [l] 直到和 [l-1] 不相等
        对 [r] 同理
        [...,[i],...,[l],...,[r-1],[r],...]

        对于为什么无论是否有 nums[l] == nums[l-1] (举例,还有一个) 
        均要进行 l+=1 r-=1:
        不移动不就一直成立了(while 和 else), 
        起不到移动 [l] [r] 来搜索其他答案的作用

        """
        nums.sort() # 从小到大
        lenth = len(nums)
        ans = []
        for i in range(lenth-2):
            # 枚举到倒数第三个元素, 为 nums[i]
            if i>0 and nums[i] == nums[i-1]:
                # 排除两个nums[i]相同的情况, 答案中不可以包含重复的三元组。
                continue

            if nums[i]+nums[i+1]+nums[i+2]>0:
                # 枚举元素 和 相邻的的两个元素(目前剩余的最小的两个元素)
                # 的 和 还小于0, 这个 [i] 和 [i+1] , [i+2] ... 都没必要尝试了
                break

            if nums[i]+nums[-1]+nums[-2]<0:
                # 枚举元素 和 整个list中最大的两个元素
                # 的 和 小于0, 这个 nums[i] 一定不够大
                # 后面会有 ?
                continue


            l = i+1 # 左
            r = lenth-1 # 右
            while l<r:
                sums = nums[l]+nums[r]+nums[i]
                if sums>0:
                    r-=1
                elif sums<0:
                    l+=1
                else:
                    # 答案
                    ans.append([nums[i],nums[l],nums[r]])

                    l+=1
                    while (l<r) and nums[l] == nums[l-1]:
                        l+=1
                    # 这里实现移动 i 直到 nums[i] 与前面不相等
                    
                    r-=1
                    while r>l and nums[r] == nums[r+1]:
                        r-=1
                    
                    # 分别排除(l,r)和前一个值相同的情况, 然后再 while
            
        return ans
# https://www.bilibili.com/video/BV1bP411c7oJ/
# @灵茶山艾府


# @lc code=end

