class Solution:
    def solution_1721_4_1(self, s: str, k: int) -> int:
        res = 0
        lastp = -1

        def solution_1721_4_2(l, r):
            nonlocal lastp, res
            while l >= 0 and r < len(s) and s[l] == s[r] and l > lastp:
                if r-l+1 >= k:
                    res += 1
                    lastp = r
                    break # find the shortest palindrome
                else:
                    l -= 1
                    r += 1
        
        for i in range(len(s)):
            solution_1721_4_2(i, i)  # odd length
            solution_1721_4_2(i, i+1)  # even length
        return res