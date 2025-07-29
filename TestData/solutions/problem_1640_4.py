class Solution:
    def solution_1640_4(self, edges: List[int]) -> int:
        res = []
        dic = collections.defaultdict(int)
        for i, n in enumerate(edges):
            dic[n] = i + dic.get(n, 0)
        for i, n in dic.items():
            if len(res) == 0:
                res = [n, i]
            else:
                temp = res
                if n > temp[0]:
                    res = [n, i]
                elif n == temp[0]:
                    if i < temp[1]:
                        res = [n, i]
        return res[1]