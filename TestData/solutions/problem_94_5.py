class Solution:
    def solution_94_5(self, s: str, t: str) -> bool:
        mapping = {}
        reverse_mapping = {}
        for cs, ct in zip(s, t):
            try:
                if mapping[cs] != ct:
                    return False
            except:
                if ct in reverse_mapping:
                    return False
                mapping[cs] = ct
                reverse_mapping[ct] = cs
        return True