class Solution:
    def solution_152_3(self, n: int, primes: List[int]) -> int:
        ans = [1]
        hp = [(p, 0) for p in primes]
        for _ in range(1, n): 
            ans.append(hp[0][0])
            while ans[-1] == hp[0][0]: 
                val, i = heappop(hp)
                val = val//(ans[i]) * ans[i+1]
                heappush(hp, (val, i+1))
        return ans[-1]