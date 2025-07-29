class Solution:
    def solution_1624_1(self, s: str) -> str:
        
        setS = set()

        for x in s:
            if x in setS:
                return x
            else:
                setS.add(x)