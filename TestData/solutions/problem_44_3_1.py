class Solution:
    def solution_44_3_1(self, s: str) -> List[List[str]]:
        l = len(s)
        
        def solution_44_3_2(s):
            return s == s[::-1]
        
        @cache
        def solution_44_3_3(start):
            if start == l:
                return []

            res = []
            for i in range(start + 1, l + 1):
                sub = s[start:i]

                if solution_44_3_2(sub):
                    subres = solution_44_3_3(i)
                    if not subres:
                        res.append(deque([sub]))
                    else:
                        for arr in subres:
                            copy = arr.copy()
                            copy.appendleft(sub)
                            res.append(copy)
    
            return res
            
        return solution_44_3_3(0)