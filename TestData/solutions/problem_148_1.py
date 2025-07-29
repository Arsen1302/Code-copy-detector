class Solution:
    def solution_148_1(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n): # Choose the length of first number
            # If length of 1st number is > 1 and starts with 0 -- skip
            if i != 1 and s[0] == '0':
                continue
            for j in range(1, n): # Choose the length of second number
                # If length of 2nd number is > 1 and starts with 0 -- skip
                if j != 1 and s[i] == '0':
                    continue

                # If the total length of 1st and 2nd number >= n -- skip
                if i + j >= n:
                    break

                # Just use the brute force approach
                a = int(s[0: i])
                b = int(s[i: i+j])
                d = i+j
                while d < n:
                    c = a + b
                    t = str(c)
                    if s[d: d + len(t)] != t:
                        break
                    d += len(t)
                    a = b
                    b = c
                if d == n:
                    return True
        return False