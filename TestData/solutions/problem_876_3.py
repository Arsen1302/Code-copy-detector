class Solution:
    def solution_876_3(self, palindrome: str) -> str:
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a': return palindrome[:i] + 'a' + palindrome[i+1:]
        return '' if len(palindrome) == 1 else palindrome[:-1] + 'b'