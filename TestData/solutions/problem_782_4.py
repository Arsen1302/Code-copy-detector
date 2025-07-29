class Solution:
    def solution_782_4(self, n: int) -> int:
        k=len([x for x in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97] if x<=n])
        return (factorial(k)*factorial(n-k))%(10**9+7)