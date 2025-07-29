class Solution:
    def solution_1327_5(self, s: str, k: int) -> int:
        s = int(''.join(map(lambda x: str(ord(x) - 96), s)))
        for i in range(k):
            s = reduce(lambda x, y: int(x) + int(y), str(s))
        return s