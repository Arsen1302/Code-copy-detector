class Solution:
    def solution_174_4_1(self, l, r, s):
        if l >= r:
            return
        s[l], s[r] = s[r], s[l]
        self.solution_174_4_1(l+1, r-1, s)

    def solution_174_4_2(self, s: List[str]) -> None:
        self.solution_174_4_1(0, len(s)-1, s)