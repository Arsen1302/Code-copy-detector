class Solution:
    def solution_1010_3(self, n: int, left: List[int], right: List[int]) -> int:
        if n==0:return 0
        if len(left)==0:return n-min(right)
        if len(right)==0:return max(left)-0
        if len(left) and len(right):
            return max(n-min(right),max(left)-0)