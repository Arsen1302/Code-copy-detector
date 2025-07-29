class Solution(object):
    def solution_1460_5(self, title):
        return " ".join(map(lambda x: x.title() if len(x)>2 else x.lower(), title.split()))