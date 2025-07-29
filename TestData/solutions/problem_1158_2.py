class Solution:
    def solution_1158_2(self, deliciousness: List[int]) -> int:
        freq = defaultdict(int)
        for x in deliciousness: freq[x] += 1
        
        ans = 0
        for x in freq: 
            for k in range(22): 
                if 2**k - x <= x and 2**k - x in freq: 
                    ans += freq[x]*(freq[x]-1)//2 if 2**k - x == x else freq[x]*freq[2**k-x]
        return ans % 1_000_000_007