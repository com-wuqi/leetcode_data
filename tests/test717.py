class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        # bits.pop()
        check=0
        i=0
        while i<len(bits)-1: # 判断到倒数第二位
            check+=1 if bits[i]==0 else 2
            i+=1 if bits[i]==0 else 2
            
        return check==len(bits)-1
    
slu=Solution()
test1=slu.isOneBitCharacter([1,0,0])
print(test1)