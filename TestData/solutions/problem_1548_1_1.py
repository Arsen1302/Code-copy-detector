class Solution:
    def solution_1548_1_1(self, par: List[int], s: str) -> int:
        dit = {}
        # store tree in dictionary
        for i in range(len(par)):
            if par[i] in dit:
                dit[par[i]].append(i)
            else:
                dit[par[i]] = [i]
                
        ans = 1        
        def solution_1548_1_2(n):
            nonlocal ans
            if n not in dit:
                return 1
            
            largest=0 # largest path lenght among all children
            second_largest=0 # second largest path lenght among all children
            for u in dit[n]:
                curr = solution_1548_1_2(u)
                if s[u]!=s[n]: # pick child path if child and parent both have different value
                    if curr>largest:
                        second_largest = largest
                        largest = curr
                    elif curr>second_largest:
                        second_largest = curr
                        
            ans = max(ans,largest+second_largest+1) # largest path including parent with at most two children 
            
            return largest+1  # return largest path end at parent
        
        solution_1548_1_2(0)
        return ans
        ```