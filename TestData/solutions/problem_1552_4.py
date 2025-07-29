class Solution:
    def solution_1552_4(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        
        # build offset at start/end timepoints
        q = defaultdict(int)
        for a, b in flowers:
            q[a] += 1
            q[b + 1] -= 1
              
        # record visitor coming time and index in answer array
        ans = [0] * len(persons)
        loc = defaultdict(set)
        for i, p in enumerate(persons):
            loc[p].add(i)
        
        # sort bloom and visitor timepoints
        q_k = sorted(q)
        loc_k = sorted([k for k in loc if k >= q_k[0] and k <= q_k[-1]]) # arrive prior to the first bloom start and after last bloom end will end up 0
        cur = 0
        
        for k in q_k:            
            cur += q[k]
            while loc_k and k >= loc_k[0]:
                t_come = loc_k.pop(0)
                for i in loc[t_come]:
                    ans[i] = cur - (k > t_come) * q[k] # if visit time prior to current bloom start/end time, then cancel offset
            if not loc_k: return ans

        return ans