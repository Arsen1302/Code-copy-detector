class Solution:
    def solution_1548_4_1(self, v):
        best, best_one, best_two = 1, 0, 0
        for c in self.children[v]:
            best_tmp, path_len = self.solution_1548_4_1(c)
            best = max(best, best_tmp)
            if self.s[v] != self.s[c]:
                if path_len > best_one:
                    best_one, best_two = path_len, best_one
                elif path_len > best_two:
                    best_two = path_len
        return max(best, best_one + best_two + 1), best_one + 1
        
    def solution_1548_4_2(self, parent: List[int], s: str) -> int:
        self.s = list(s)
        self.children = defaultdict(set)
        [self.children[p].add(c) for c, p in enumerate(parent) if p >= 0]
        return self.solution_1548_4_1(0)[0]