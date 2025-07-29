class Solution:
    def solution_440_4(self, n: int) -> int:
        n = str(n)
        n = list(n)
        n[0] = int(n[0])
        for i in range(1, len(n)):
            n[i] = int(n[i])
            if n[i] < n[i-1]:
                for j in range(i-1, -1, -1):
                    if n[j+1] < n[j]:
                        n[j] = n[j] - 1
                        n[j+1] = 9
                for k in range(i, len(n)):
                    n[k] = 9
                break

                
        res = n[0]
        for i in range(1, len(n)):
            res *= 10
            res += n[i]
        return res