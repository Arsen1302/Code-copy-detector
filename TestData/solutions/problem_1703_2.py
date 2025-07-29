class Solution:
    def solution_1703_2(self, queries, dictionary):
        n, ans = len(queries[0]), []

        for i in queries:
            for j in dictionary:
                if sum(i[k] != j[k] for k in range(n)) < 3:
                    ans.append(i)
                    break

        return ans