class Solution:
    def solution_557_4(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        take = {}
        for b in sorted(B, reverse=True):
            if b < A[-1]: 
                take.setdefault(b, []).append(A.pop())
        return [(take.get(b, []) or A).pop() for b in B]