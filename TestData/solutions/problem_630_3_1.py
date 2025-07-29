class Solution:
    def solution_630_3_1(self, arr: List[int]) -> str:
        
        def solution_630_3_2(i): 
            """Return unique permutations of arr."""
            if i == 4: yield arr
            else: 
                seen = set()
                for ii in range(i, 4):
                    if arr[ii] not in seen: 
                        seen.add(arr[ii])
                        arr[i], arr[ii] = arr[ii], arr[i]
                        yield from solution_630_3_2(i+1)
                        arr[i], arr[ii] = arr[ii], arr[i]
        
        hh = mm = -1
        for x in solution_630_3_2(0):
            h = 10*x[0] + x[1]
            m = 10*x[2] + x[3]
            if h < 24 and m < 60: hh, mm = max((hh, mm), (h, m))
        return f"{hh:02}:{mm:02}" if hh > -1 else ""