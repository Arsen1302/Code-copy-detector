class Solution:
    def solution_1450_1_1(self, s: str, locked: str) -> bool:
        def solution_1450_1_2(s: str, locked: str, op: str) -> bool:
            bal, wild = 0, 0
            for i in range(len(s)):
                if locked[i] == "1":
                    bal += 1 if s[i] == op else -1
                else:
                    wild += 1
                if wild + bal < 0:
                    return False
            return bal <= wild
        return len(s) % 2 == 0 and solution_1450_1_2(s, locked, '(') and solution_1450_1_2(s[::-1], locked[::-1], ')')