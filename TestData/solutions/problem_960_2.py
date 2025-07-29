class Solution:
    def solution_960_2(self, paths: List[List[str]]) -> str:
        d = dict(paths)
        for i in d.values():
            if i not in d.keys():
                return i