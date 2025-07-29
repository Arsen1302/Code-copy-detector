class Solution:

    def solution_653_5_1(self, n: str) -> float:
        if "." not in n:
            return float(n)
        whole, dec = n.split(".")
        if dec:
            if "(" in dec:
                idx_bracket = dec.index("(")
                return float(f"{whole}.{dec[:idx_bracket]}{dec[idx_bracket + 1: -1] * 17}")
            return float(f"{whole}.{dec}")
        return float(f"{whole}.")

    def solution_653_5_2(self, s: str, t: str) -> bool:
        return abs(self.solution_653_5_1(s) - self.solution_653_5_1(t)) < 1e-16