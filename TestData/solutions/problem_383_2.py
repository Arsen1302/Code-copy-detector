class Solution:
    def solution_383_2(self, m: str) -> bool:
        return m.count("D") == m.count("U") and m.count("R") == m.count("L")