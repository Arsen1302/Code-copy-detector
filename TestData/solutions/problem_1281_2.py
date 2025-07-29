class Solution:
    def solution_1281_2(self, n: str, x: int) -> str:
        digit = str(x)
        if n[0] == "-":
            for i, d in enumerate(n[1:]):
                if d > digit:
                    return f"{n[:i + 1]}{digit}{n[i + 1:]}"
        else:
            for i, d in enumerate(n):
                if d < digit:
                    return f"{n[:i]}{digit}{n[i:]}"
        return n + digit