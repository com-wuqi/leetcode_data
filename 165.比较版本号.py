#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#


# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = version1.split(".")
        version2_list = version2.split(".")

        max_length = max(len(version1_list), len(version2_list))
        min_lenth = min(len(version1_list), len(version2_list))

        if (max_length - min_lenth) != 0:
            if len(version1_list) > len(version2_list):
                version2_list+=[0,]*(max_length - min_lenth)
            else:
                version1_list+=[0,]*(max_length - min_lenth)

        for i in range(0, max_length):
            v1 = version1_list[i]
            v2 = version2_list[i]
            if int(v1) < int(v2):
                return -1
            elif int(v1) > int(v2):
                return 1
            else:
                pass
        return 0


# @lc code=end
