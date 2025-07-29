class Solution:
    def solution_1108_2(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp = {x[0]: x for x in pieces}
        return sum((mp.get(x, []) for x in arr), []) == arr