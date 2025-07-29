class Solution:
    """
    dp -> key: i value: amount of deliciousness == i
    for d in 2**0, 2**1, ..., 2**21
    why 2**21: max of deliciousness is 2*20, sum of 2 max is 2**21
    O(22*N)
    """
    def solution_1158_3(self, ds: List[int]) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        # ds.sort() # no need to sort
        res = 0
        
        for d in ds:
            for i in range(22):
                # if 2**i - d in dp:
                res += dp[2**i - d]
            dp[d] += 1
        return res % (10**9 + 7)