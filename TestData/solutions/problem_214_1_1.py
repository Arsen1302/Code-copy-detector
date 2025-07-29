class Solution(object):
    def solution_214_1_1(self, stones):
        n = len(stones)
        stoneSet = set(stones)
        visited = set()
        def solution_214_1_2(value,units):
            if (value+units not in stoneSet) or ((value,units) in visited):
                return False
            if value+units == stones[n-1]:
                return True
            visited.add((value,units))
            return solution_214_1_2(value+units,units) or solution_214_1_2(value+units,units-1) or solution_214_1_2(value+units,units+1)
        return solution_214_1_2(stones[0],1)