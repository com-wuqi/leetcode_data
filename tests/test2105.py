class Solution:
    def minimumRefill(self, plants: list[int], capacityA: int, capacityB: int) -> int:
        Alice = 0
        Bob = len(plants) - 1
        # 位置
        ans = 0
        A, B = capacityA, capacityB  # 当前水罐
        while Alice < Bob:
            if A > plants[Alice]:
                A -= plants[Alice]
            else:
                ans += 1
                A = capacityA  # recoery
                A -= plants[Alice]
            Alice += 1
            if B > plants[Bob]:
                B -= plants[Bob]
            else:
                ans += 1
                B = capacityB
                B -= plants[Bob]
            Bob-=1
        """
        这样就卡死了, 
        如果继续,我们需要在每个 if 后面判断 Alice 和 Bob 是否在同一个位置上
        考虑翻转 if , 重构
        """
