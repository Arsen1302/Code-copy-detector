class Solution:
    def solution_1400_2_1(self, n: int) -> int:
        
        def solution_1400_2_2(i, x):
            if i == k:
                if all(d == v for d, v in freq.items() if v): yield x
            else: 
                for d in range(1, k+1):
                    if freq[d] < d <= freq[d] + k - i: 
                        freq[d] += 1
                        yield from solution_1400_2_2(i+1, 10*x+d)
                        freq[d] -= 1

        for k in (len(str(n)), len(str(n))+1):
            freq = Counter()
            for val in solution_1400_2_2(0, 0):
                if val > n: return val