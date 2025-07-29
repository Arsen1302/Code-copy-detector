class Solution:
    def solution_918_5 (self, m: List[List[int]]) -> List[int]:
        min_r = [min(x) for x in m]
        max_c = []
        for i in range(len(m[0])):
            tmp = []
            for j in range(len(m)):
                tmp.append(m[j][i])
            max_c.append(max(tmp))
        return set(min_r)&amp;set(max_c)