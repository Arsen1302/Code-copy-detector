class Solution:
    def solution_607_5(self, name: str, typed: str) -> bool:
        g1 = [(k, len(list(grp))) for k, grp in itertools.groupby(name)]
        g2 = [(k, len(list(grp))) for k, grp in itertools.groupby(typed)]
        if len(g1) != len(g2):
            return False
        for i in range(len(g1)):
            if g1[i][0] != g2[i][0] or g1[i][1] > g2[i][1]:
                return False
        return True