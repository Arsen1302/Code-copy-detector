class Solution:
    def solution_1580_2(self, s: str, d: int) -> str:
            return ' '.join((f"${(int(w[1:])*(1-(d/100))):.2f}" if w.startswith('$') and w[1:].isnumeric() else w for w in s.split()))