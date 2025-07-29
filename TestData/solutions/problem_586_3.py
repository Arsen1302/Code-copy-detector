class Solution:
    def solution_586_3(self, digits: List[str], n: int) -> int:
        s = str(n)
        ans = sum(len(digits) ** i for i in range(1, len(s)))
        for i in range(len(s)): 
            ans += sum(c < s[i] for c in digits) * (len(digits) ** (len(s) - i - 1))
            if s[i] not in digits: return ans
        return ans + 1