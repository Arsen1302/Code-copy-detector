class Solution:
    def solution_398_5_1(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        
        def solution_398_5_2(start, end): 
            """Return min steps to move from start to end."""
            ans = 0 
            seen = {start}
            queue = deque([start])
            while queue: 
                for _ in range(len(queue)): 
                    i, j = queue.popleft()
                    if (i, j) == end: return ans
                    for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                        if 0 <= ii < m and 0 <= jj < n and forest[ii][jj] != 0 and (ii, jj) not in seen: 
                            seen.add((ii, jj))
                            queue.append((ii, jj))
                ans += 1
            return -1 
        
        ans = 0 
        start = (0, 0)
        for _, i, j in sorted((forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j] > 1): 
            val = solution_398_5_2(start, (i, j))
            if val == -1: return -1 
            ans += val 
            start = (i, j)
        return ans