class Solution:
    def solution_625_2(self, A: List[str]) -> int:
        
        res = 0
        for pos in range(len(A[0])):
            for word in range(len(A)-1):
                if A[word][pos] > A[word+1][pos]:
                    res += 1
                    break
        return res