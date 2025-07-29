class Solution:
    def solution_733_5(self, matrix: List[List[int]]) -> int:
        d = collections.defaultdict(int)                                              # hashmap for counting
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            reverse = not matrix[i][0]                                                # decide whether need to reverse bit
            cur = ''.join(['0' if matrix[i][j] ^ reverse else '1' for j in range(n)]) # see below solution for expanded code
            d[cur] += 1                                                               # count frequency
        return max(d.values())