class Solution:
    def solution_933_3(self, S, K):
        return bin(reduce(operator.xor, map(lambda x: 1 << (ord(x) - 97), S))).count('1') <= K <= len(S)