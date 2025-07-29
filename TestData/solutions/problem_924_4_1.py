class Solution:
    @cache
    def solution_924_4_1(self, l, r, c):
        if c == 0 or l >= r:
            return 0
		return max(self.slices[l] + self.solution_924_4_1(l+2, r, c-1), self.solution_924_4_1(l+1, r, c)) # To select or not to select the current slice
		
    def solution_924_4_2(self, slices: List[int]) -> int:
        self.slices = slices + slices
        return max(self.slices[i] + self.solution_924_4_1(i + 2, i - 1 + len(slices), len(slices) // 3 - 1) for i in range(-3, 3)) # Handling the circular condition