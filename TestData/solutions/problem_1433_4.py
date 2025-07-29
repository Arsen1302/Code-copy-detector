class Solution:
    def solution_1433_4(self, digits: List[int]) -> List[int]:
        
        return sorted({i*100 + j*10 + k for i,j,k in permutations(digits,3) if i!=0 and k%2==0})