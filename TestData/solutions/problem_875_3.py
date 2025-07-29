class Solution:
    def solution_875_3(self, n: int, ranges: List[int]) -> int:
        start, end = 0, 0
        taps = 0
        
        while end< n:
            for i in range(len(ranges)):
                if i-ranges[i] <= start and i+ ranges[i]>end:
                    end = i + ranges[i]
            if start == end:
                return -1
            taps +=1
            start = end
        return taps