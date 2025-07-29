class Solution:
    def solution_1450_2(self, s: str, locked: str) -> bool:
        if len(s)&amp;1: return False
        bal = 0
        for ch, lock in zip(s, locked):
            if lock == '0' or ch == '(': bal += 1
            elif ch == ')': bal -= 1
            if bal < 0: return False 
        bal = 0
        for ch, lock in zip(reversed(s), reversed(locked)): 
            if lock == '0' or ch == ')': bal += 1
            elif ch == '(': bal -= 1
            if bal < 0: return False
        return True