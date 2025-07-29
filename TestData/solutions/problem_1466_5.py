class Solution:
    def solution_1466_5(self, startWords: List[str], targetWords: List[str]) -> int:
        startWords = set([reduce(lambda res, c: res ^ (1 << (ord(c) - ord('a'))), word, 0) for word in startWords])
        return len(list(filter(lambda tup: any(tup[0] ^ (1 << (ord(c) - ord('a'))) in startWords for c in tup[1]), list(zip([reduce(lambda res, c: res ^ (1 << (ord(c) - ord('a'))), word, 0) for word in targetWords], targetWords)))))