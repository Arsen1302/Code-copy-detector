class Solution:
    
    def solution_1721_3_1(self, s: str, k: int) -> int:
        n = len(s)
        # function to check whether substring is a palindrome
        def solution_1721_3_2(i, j):
            # if end index is greater then length of string
            if j > len(s):
                return False
            if s[i : j] == s[i : j][::-1]:
                return True
            return False
        maxSubstrings = 0
        start = 0
        while start < n:
            if solution_1721_3_2(start, start + k):
                maxSubstrings += 1
                start += k
            elif solution_1721_3_2(start, start + k + 1):
                maxSubstrings += 1
                start += k + 1
            else:
                # when there is no palindrome starting at that particular index   
                start += 1
        return maxSubstrings