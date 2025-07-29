class Solution:
    def solution_948_5(self, s: str) -> str:
        x = [c for c in s if c.isalpha()]
        y = [c for c in s if c.isdigit()]
        if len(x) < len(y):
            x, y = y, x
        if len(x) == len(y) or len(y) + 1 == len(x):
            return "".join(f"{x}{y}" for x, y in zip_longest(x, y, fillvalue=""))
        else:
            return ""