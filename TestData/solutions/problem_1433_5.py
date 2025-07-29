class Solution:
    def solution_1433_5(self, digits: List[int]) -> List[int]:
        return [''.join([str(i) for i in x]) for x in sorted(set(permutations(digits,3))) if x[2]%2==0 and x[0]!=0]