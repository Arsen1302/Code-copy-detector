class Solution(object):
    def solution_1076_5(self, text):
        return "".join(text.split()) + " " * text.count(" ") if len(text.split()) <= 1 else (" " * (text.count(" ")//(len(text.split())-1))).join(text.split()) + " " * (text.count(" ") % (len(text.split())-1))