class Solution:
    def solution_1631_2(self, i1: List[List[int]], i2: List[List[int]]) -> List[List[int]]:
        return sorted((Counter({i[0] : i[1] for i in i1}) + Counter({i[0] : i[1] for i in i2})).items())