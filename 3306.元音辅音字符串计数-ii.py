#
# @lc app=leetcode.cn id=3306 lang=python3
#
# [3306] 元音辅音字符串计数 II
#

# @lc code=start
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        """
        这道题也是三指针滑窗
        也就是说, 当 越长越合法 时, right 不参与答案构成
        事实上, 就是两个 越长越合法 做差, 写两遍 (灵神的思路)
        越长越合法 和 其他滑窗(包括 越短越合法) 的主要区别是:
        我们需要让 left 在循环结束时(while后)不合法, 
        所以在 条件成立 时进入 while,
        使条件不符合, 即 left-1 合法 !
        其他滑窗在刚刚不符合要求时(比如大于k)时进入 while ,
        即进入while时 left 不合法, 移动后的 left 合法
        tip:
        关于 left1 为什么 大于 left2 :)
        更要严格的条件需要移动更多次, 显然
        """
        dict1={"a":0,"e":0,"i":0,"o":0,"u":0}
        dict2={"a":0,"e":0,"i":0,"o":0,"u":0}
        cnt1=cnt2=0 # 统计辅音字母的个数
        left1=left2=0
        ans=0
        for data in word:
            if data in "aeiou":
                dict1[data]+=1
                dict2[data]+=1
            else:
                cnt1+=1
                cnt2+=1
            while 0 not in dict1.values() and cnt1>=k:
                # 字母均存在 辅音数大于等于k
                if word[left1] in "aeiou":
                    dict1[word[left1]]-=1
                else:
                    cnt1-=1
                left1+=1
            while 0 not in dict2.values() and cnt2>=k+1:
                if word[left2] in "aeiou":
                    dict2[word[left2]]-=1
                else:
                    cnt2-=1
                left2+=1
            ans+=left1-left2
        return ans
        
# @lc code=end

