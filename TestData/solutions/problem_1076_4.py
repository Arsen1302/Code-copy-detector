class Solution(object):
    def solution_1076_4(self, text):
        w, s = len(text.split()), text.count(" ")
        q, r = (divmod(s, (w - 1))) if w > 1 else (0, s)
        return (" " * q).join(text.split()) + " " * r