class Solution:
    def solution_876_1(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1: return ''
        for i, c in enumerate(palindrome):
            if c != 'a' and ((i != n // 2 and n % 2) or not n % 2): return palindrome[:i] + 'a' + palindrome[i+1:]                
        else: return palindrome[:-1] + 'b'