class Solution:
    def solution_152_2(self, n: int, primes: List[int]) -> int:
        ans = [1]
        ptr = [0]*len(primes) #all pointing to 0th index
        for _ in range(1, n): 
            ans.append(min(ans[ptr[i]]*p for i, p in enumerate(primes)))
            for i, p in enumerate(primes):
                if ans[ptr[i]] * p == ans[-1]: ptr[i] += 1
        return ans[-1]