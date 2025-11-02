#
# @lc app=leetcode.cn id=2105 lang=python3
#
# [2105] 给植物浇水 II
#


# @lc code=start
class Solution:
    def minimumRefill(self, plants: list[int], capacityA: int, capacityB: int) -> int:
        Alice = 0
        Bob = len(plants) - 1
        # 位置
        ans = 0
        A, B = capacityA, capacityB  # 当前水罐
        while Alice < Bob:

            if A < plants[Alice]:
                ans += 1
                A = capacityA  # recoery
            
            if B < plants[Bob]:
                ans += 1
                B = capacityB
            
            
            A -= plants[Alice]
            Alice += 1
            
            B -= plants[Bob]
            Bob -= 1

            # if Alice==Bob and max(A,B)>=plants[Alice]: # 同时到达, 水量足够
            #     if A>B:
            #         pass
            #     # 最后一次谁浇水就不重要了, 我们不需要统计谁浇了几次水
            #     # 所以翻转 if , 考虑两人均水不够
            if Alice == Bob and max(A, B) < plants[Alice]:
                ans += 1

        return ans


# @lc code=end
