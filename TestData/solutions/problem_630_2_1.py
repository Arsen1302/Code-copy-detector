class Solution:
    def solution_630_2_1(self, A: List[int]) -> str:
        
        def solution_630_2_2(i=0): 
            """Return all solution_630_2_2 via generator."""
            if i == len(A): yield A
            for ii in range(i, len(A)): 
                A[i], A[ii] = A[ii], A[i]
                yield from solution_630_2_2(i+1)
                A[i], A[ii] = A[ii], A[i]
        
        hh = mm = -1
        for x in solution_630_2_2(): 
            h = 10*x[0] + x[1]
            m = 10*x[2] + x[3]
            if h < 24 and m < 60 and 60*hh + mm < 60*h + m: hh, mm = h, m 
        return f"{hh:02}:{mm:02}" if hh >= 0 else ""