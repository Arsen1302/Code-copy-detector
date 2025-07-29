class Solution:
    def solution_586_2(self, digits: List[str], n: int) -> int:
        s = str(n)
        prev = 1
        for i, ch in enumerate(reversed(s)): 
            k = bisect_left(digits, ch)
            ans = k*len(digits)**i
            if k < len(digits) and digits[k] == ch: ans += prev 
            prev = ans
        return ans + sum(len(digits)**i for i in range(1, len(s)))