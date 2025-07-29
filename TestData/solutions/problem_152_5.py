class Solution:
    def solution_152_5(self, n, primes):
        ans = [1]

        while n:
            val = heappop(ans)

            while ans and ans[0] == val:
                heappop(ans)

            for p in primes:
                heappush(ans,p*val)

            n -= 1

        return val