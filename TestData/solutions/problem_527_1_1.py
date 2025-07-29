class Solution:
    def solution_527_1_1(self, strs: List[str]) -> int:
        N = len(strs)
        parent = [i for i in range(N)]
        depth = [1 for _ in range(N)]

        def solution_527_1_2(idx):
            if idx != parent[idx]:
                return solution_527_1_2(parent[idx])
            return idx
        
        def solution_527_1_3(idx1, idx2):
            p1 = solution_527_1_2(idx1)
            p2 = solution_527_1_2(idx2)
            if p1 == p2: return
            if depth[p1] < depth[p2]:
                parent[p1] = p2
            elif depth[p2] < depth[p1]:
                parent[p2] = p1
            else:
                parent[p2] = p1
                depth[p1] += 1

        def solution_527_1_4(w1, w2):
            dif_idx = -1
            for idx in range(len(w1)):
                if w1[idx] != w2[idx]:
                    if dif_idx < 0:
                        dif_idx = idx
                    else:
                        if w1[dif_idx] != w2[idx]: return False
                        if w2[dif_idx] != w1[idx]: return False
                        if w1[idx+1:] != w2[idx+1:]: return False
                        return True
            return True
                    
        for idx in range(1, N):
            for pid in range(0, idx):
                if solution_527_1_4(strs[pid], strs[idx]):
                    solution_527_1_3(pid, idx)

        return len([i for i, p in enumerate(parent) if i==p])