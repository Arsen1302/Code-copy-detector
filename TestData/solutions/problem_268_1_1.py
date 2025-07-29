class Solution:
    def solution_268_1_1(self, strs: List[str], m: int, n: int) -> int:
        counter=[[s.count("0"), s.count("1")] for s in strs]
        
        @cache
        def solution_268_1_2(i,j,idx):
            if i<0 or j<0:
                return -math.inf
            
            if idx==len(strs):
                return 0
            
            return max(solution_268_1_2(i,j,idx+1), 1 + solution_268_1_2(i-counter[idx][0], j-counter[idx][1], idx+1))
        return solution_268_1_2(m,n,0)