class Solution:
    def solution_1343_4(self, patterns: List[str], word: str) -> int:
        li = list(map(lambda x: x in word, patterns))
        return li.count(True)