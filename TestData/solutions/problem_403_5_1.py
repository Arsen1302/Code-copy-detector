class Solution:
    def solution_403_5_1(self, a: str, b: str) -> int:
        
        def solution_403_5_2(pattern):
            # kmp failure function
            m = len(pattern)
            f = [0] * m
            i = 1
            j = 0
            while i < m:
                if pattern[j] == pattern[i]:
                    f[i] = j+1
                    i += 1
                    j += 1
                elif j > 0:
                    j = f[j-1]
                else:
                    f[i] = 0
                    i += 1
            return f
        
        f = solution_403_5_2(b)
        n = len(a)
        m = len(b)
        i = 0
        j = 0
        while i < n + m:  # worst case, start of b begins at end of a
            if b[j] == a[i%n]:
                if j == m-1:
                    return math.ceil((i+1) / n)
                i += 1
                j += 1
            elif j > 0:
                j = f[j-1]
            else:
                i += 1
        return -1