class Solution:
    def solution_248_3(self, n: List[int]) -> List[int]:
        i, L = 0, len(n)
        while i != L:
        	if n[i] in [i + 1, n[n[i] - 1]]: i += 1
        	else: n[n[i] - 1], n[i] = n[i], n[n[i] - 1]
        return [i + 1 for i in range(L) if n[i] != i + 1]