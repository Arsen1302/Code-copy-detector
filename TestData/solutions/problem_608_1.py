class Solution:
    def solution_608_1(self, s: str) -> int:
        """
                     0 0 1 1 0
        oneCount:    0 0 1 2 2
        zeroCount:   1 1 0 0 1
        flipCount:   0 0 0 0 1
        
        
                     0 1 0 1 0
        oneCount:    0 1 1 2 2
        zeroCount:   1 0 1 1 2
        flipCount:   0 0 1 1 2
        
                     0 0 0 1 1 0 0 0
        oneCount:    0 0 0 1 2 2 2 2
        zeroCount:   1 1 1 0 0 1 2 3
        flipCount:   0 0 0 0 0 1 2 2
        """
        oneCount = 0
        zeroCount = 0
        flipCount = 0
        for c in s:
            if c == "1":
                oneCount += 1
            if c == "0":
                zeroCount += 1
            flipCount = min(zeroCount,oneCount)
            zeroCount = flipCount
        return flipCount