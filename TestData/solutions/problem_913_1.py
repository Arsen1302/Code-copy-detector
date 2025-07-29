class Solution:
    def solution_913_1(self, n: int) -> str:
        a="a"
        b="b"
        if n%2==0:
            return (((n-1)*a)+b)
        return (n*a)