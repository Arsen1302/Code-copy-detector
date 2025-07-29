class Solution:
    def solution_1153_4(self, s: str) -> bool:
        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        n = len(s)
        m = n // 2
        return sum(s[i] in vowels for i in range(m)) == sum(s[i] in vowels for i in range(m, n))