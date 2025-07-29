class Solution:
    def solution_554_2(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(map(list,zip(*matrix))) # we need to explicitly cast as zip returns tuples