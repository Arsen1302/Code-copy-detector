class Solution:
#     O(n) || O(1)
    def solution_355_4(self, flowerbed: List[int], n: int) -> bool:
        f = flowerbed
        for i in range(len(f)):
            leftOk = i == 0 or f[i-1] == 0
            rightOk = i == len(f) -1 or f[i+1] == 0
            if leftOk and f[i] == 0 and rightOk:
                f[i] = 1
                n -= 1
        return n <= 0