class Solution:
    def solution_77_3(self, title: str) -> int:
        return reduce(lambda x,y: x * 26 + y, map(lambda x: ord(x)-ord('A')+1,title))