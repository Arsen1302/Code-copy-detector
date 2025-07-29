class Solution:
    def solution_1303_5(self, s: str, part: str) -> str:
        string=s.replace(part,"",1)
        while part in string:
            string=string.replace(part,"",1)
        return string