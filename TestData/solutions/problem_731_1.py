class Solution:
    def solution_731_1(self, B: List[int]) -> List[int]:
        L, A, i = len(B), [0]*len(B), 0
        for k,v in collections.Counter(B).most_common():
            for _ in range(v):
                A[i], i = k, i + 2
                if i >= L: i = 1
        return A



class Solution:
    def solution_731_1(self, B: List[int]) -> List[int]:
        L, C = len(B), collections.Counter(B)
        B.sort(key = lambda x: (C[x],x))
        B[1::2], B[::2] = B[:L//2], B[L//2:]
        return B
		
		
- Junaid Mansuri