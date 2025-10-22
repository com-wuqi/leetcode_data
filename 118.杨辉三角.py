#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#


# @lc code=start
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:

        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        if numRows >30:
            raise RuntimeError
        # 排除特殊情况, 1 <= numRows <= 30

        result = [[1], [1, 1]]
        for lineindex in range(2, numRows):
            # 第三行的索引为2, 循环至(numRows-1)即numRows行的索引
            buildlist = (
                [
                    1,
                ]
                + [None] * (lineindex - 1)
                + [
                    1,
                ]
            ) # 第三行需要填充1个None, 即(lineindex-1)个, 以此类推
            for index, _ in enumerate(buildlist):
                if index == 0 or index == len(buildlist) - 1:
                    pass  # 排除首尾两个元素
                else:
                    buildlist[index] = (
                        result[lineindex - 1][index - 1] + result[lineindex - 1][index]
                    )
                # 回溯上一行
            result.append(buildlist)

        return result


# @lc code=end
