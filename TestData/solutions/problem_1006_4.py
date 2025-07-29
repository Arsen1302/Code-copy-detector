class Solution:
    def solution_1006_4(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        if n % 2 !=  0:
            return False
        tmp = []
        for i in range(n):
            tmp.append(arr[i] % k)
        
        zero = [n for n in tmp if n == 0]
        unzero = [n for n in tmp if n != 0]
        if len(zero) % 2 != 0:
            return False
        unzero.sort()
        m = len(unzero)
        for i in range(m):
            if unzero[i] + unzero[m - 1 - i] != k:
                return False
        return True