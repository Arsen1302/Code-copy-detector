class Solution:
    # DFS
    def solution_542_1_1(self, A: str, B: str) -> int:
        N = len(A)
        def solution_542_1_2(A, B, pos):
            if A == B:
                return 0
            
            while A[pos] == B[pos]:
                pos += 1
                
            minCnt = float('inf')
            for i in range(pos + 1, N):
                if B[i] == A[pos] and B[i] != A[i]:
                    B[i], B[pos] = B[pos], B[i]
                    tmp = solution_542_1_2(A, B, pos + 1) + 1
                    minCnt = min(tmp, minCnt)
                    B[i], B[pos] = B[pos], B[i]
                    
            return minCnt
        
        return solution_542_1_2(list(A), list(B), 0)

    # DFS with memorization
    def solution_542_1_3(self, A: str, B: str) -> int:
        N = len(A)
        def solution_542_1_2(A, B, pos):
            sB = ''.join(B)
            if sB in map:
                return map[sB]
            
            if A == B:
                return 0
            
            while A[pos] == B[pos]:
                pos += 1
                
            minCnt = float('inf')
            for i in range(pos + 1, N):
                if B[i] == A[pos] and B[i] != A[i]:
                    B[i], B[pos] = B[pos], B[i]
                    tmp = solution_542_1_2(A, B, pos + 1) + 1
                    minCnt = min(tmp, minCnt)
                    B[i], B[pos] = B[pos], B[i]
                    
            map[sB] = minCnt
            return minCnt
                    
        map = collections.defaultdict()
        return solution_542_1_2(list(A), list(B), 0)
    
    # BFS
    def solution_542_1_4(self, A: str, B: str) -> int:
        N = len(B)
        q = collections.deque([B])
        visited = set(B)
        
        cnt = 0
        pos = 0
        while q:
            qSize = len(q)
            
            for _ in range(qSize):
                cur = q.popleft()
                if cur == A:
                    return cnt
                
                pos = 0
                while cur[pos] == A[pos]:
                    pos += 1
                
                lCur = list(cur)
                for i in range(pos + 1, N):
                    if lCur[i] == A[pos] and lCur[i] != A[i]:
                        lCur[i], lCur[pos] = lCur[pos], lCur[i]
                        
                        sCur = ''.join(lCur)
                        if sCur not in visited:
                            q.append(sCur)
                            
                        visited.add(sCur)
                        lCur[i], lCur[pos] = lCur[pos], lCur[i]
            cnt += 1
            
        return cnt