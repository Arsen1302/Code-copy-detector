class Solution:
    def solution_732_3(self, s: str, t: str) -> str:
        if not s: return t
        if not t: return s
        s, t = (s, t) if len(s) <= len(t) else (t, s)
        if t[:len(s)] == s:
            return self.solution_732_3(t[len(s):], s)
        return ''