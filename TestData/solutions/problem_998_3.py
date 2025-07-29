class Solution:
    def solution_998_3(self, names: List[str]) -> List[str]:
        res = {}
        for i in names:
            candidate = i
            while candidate in res:
                candidate = i+f'({res[i]})'
                res[i] += 1
            res[candidate] = 1
        return list(res.keys())