class Solution:
    def solution_626_2(self, A: List[int]) -> int:
        A.sort()
        count = 0
        for i in range(1, len(A)):
            cur = A[i]
            prev = A[i-1]
            if(prev >= cur ):
                A[i] = prev + 1
                count += prev - cur + 1
        return count