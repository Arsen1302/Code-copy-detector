class Solution:
    def solution_94_4(self, s: str, t: str) -> bool:
        mapping = {}
        for cs, ct in zip(s, t):
            try:
                if mapping[cs] != ct:
                    return False
            except:
                if ct in mapping.values():
                    return False
                mapping[cs] = ct
        return True