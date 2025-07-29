class Solution:
    def solution_1044_4_1(self, n: int, cuts: List[int]) -> int:
        @cache
        def solution_1044_4_2(start,end):
            # Base case if start == end, no cuts can be made
            if start == end:
                return 0

            # Keep track of lowest cut, start at infinity so we can do min(res, newResult)
            res = float('inf')

            # For every cut, check if it is within the range of your start and end.
            # If it is within range, add length of current ruler to result then cut it and perform solution_1044_4_2 on both sides of the cut
            for cut in cuts:
                if start < cut < end:
                    tryCut = end-start
                    startToCut = solution_1044_4_2(start,cut)
                    cutToEnd = solution_1044_4_2(cut,end)
                    newResult = tryCut+startToCut+cutToEnd
                    res = min(res,newResult)
            
            # If no cut was possible, return 0 else return res
            return res if res != float('inf') else 0

        return solution_1044_4_2(0,n)