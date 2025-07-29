class Solution:
    def solution_1236_3(self, logs: List[List[int]], k: int) -> List[int]:
        d = {}
        for i in logs:
            if i[0] in d:
                if i[1] not in d[i[0]]:
                    d[i[0]] = d[i[0]] + [i[1]]
            else:
                d[i[0]] = [i[1]]
        res = [0]*k
        for i in d.values():
            res[len(i)-1] += 1
        return res