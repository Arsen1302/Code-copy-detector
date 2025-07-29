class Solution:
    def solution_707_5(self, A: List[int]) -> int:
        # Method 1
        # Iterative with trim, beats ~85% runtime
        res = 1
        idx = defaultdict(list)  # reverse idx
        for i, a in enumerate(A):
            idx[a] += i,
        visited = set()
        for i in range(len(A)-1):
            if idx[A[i]][0] != i:
                continue  # if the same number has been checked before, skip it
            for j in range(i+1, len(A)):
                diff = A[j] - A[i]
                if (A[i], diff) in visited:
                    continue
                visited.add((A[i], diff))
                cnt = 1
                nxt = A[j]
                pntr = i
                while nxt in idx:
                    if idx[nxt][-1] <= pntr:
                        break
                    visited.add((nxt, diff))
                    cnt += 1
                    pntr = min([_ for _ in idx[nxt] if _ > pntr])
                    nxt += diff
                res = max(res, cnt)
        return res
        
        # # Method 2:
        # # dp[i][j]: length of the longest subseq with i-th item as last item and j-500 as diff, beats ~24% runtime
        dp = [[0] * 1001 for _ in range(len(A))]
        res = 2
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff+500] = max(2, dp[j][diff+500]+1)
                res = max(res, dp[i][diff+500])
        return res
    
        # Method 3: optimize on method 2, shorter
        # dp[i] keeps a dict of <diff, length of longest subseq with i-th item as end and diff as gap>
        dp = [defaultdict(int) for _ in range(len(A))]
        res = 2
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] = max(2, dp[j][diff]+1)
                res = max(res, dp[i][diff])
        return res