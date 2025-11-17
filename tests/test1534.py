class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        ans = 0
        for i1, d1 in enumerate(arr[0:len(arr)-2]):
            for i2, d2 in enumerate(arr[i1 + 1 :len(arr)-1]):
                for _, d3 in enumerate(arr[i1 + i2 + 2 :]):
                    if abs(d1 - d2) <= a and abs(d2 - d3) <= b and abs(d1 - d3) <= c:
                        print(f"{d1} {d2} {d3}")
                        ans += 1
                    print(f"{d1} {d2} {d3}")
                    # print(f"{i1} {i2} {_}")
        return ans

slu=Solution()
test1=slu.countGoodTriplets([1,2,3,4],7,2,3)
print(test1)