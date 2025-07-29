class Solution:
    def solution_1250_5(self, n: int, k: int) -> int:
        cnt = 0
        while n:
            cnt += (n % k)
            n //= k
        print(cnt)
        return cnt