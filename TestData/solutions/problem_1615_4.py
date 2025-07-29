class Solution:
    letters = {"L", "R"}
    def solution_1615_4(self, start: str, target: str) -> bool:
        start_idx = [(c, i) for i, c in enumerate(start)
                     if c in Solution.letters]
        target_idx = [(c, i) for i, c in enumerate(target)
                      if c in Solution.letters]
        if len(start_idx) != len(target_idx):
            return False
        for (s, i), (t, j) in zip(start_idx, target_idx):
            if s == t:
                if s == "L" and i < j:
                    return False
                elif s == "R" and i > j:
                    return False
            else:
                return False
        return True