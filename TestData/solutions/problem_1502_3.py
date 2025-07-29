class Solution:
    def solution_1502_3(self, words: List[str], pref: str) -> int:
		return sum([1 for i in words if i[:len(pref)]==pref])