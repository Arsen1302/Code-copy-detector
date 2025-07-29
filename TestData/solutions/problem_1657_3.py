class Solution:
    def solution_1657_3(self, matrix, numSelect):
        m, n = len(matrix), len(matrix[0])

        list_combinations, dict2 = list(combinations({i for i in range(n)},n-numSelect)), defaultdict(int)

        for i in list_combinations:
            res = set()
            for j in i:
                for k in range(m):
                    if matrix[k][j] == 1:
                        res.add(k)

            dict2[i] = m - len(res)

        return max(dict2.values())