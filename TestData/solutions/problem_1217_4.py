class Solution:
    def solution_1217_4(self, s1: str, s2: str) -> bool:
        c=0
        set_1 = set()
        set_2 = set()
        l = len(s1)
        for i in range(l):
            if s1[i]!=s2[i]:
                set_1.add(s2[i])
                set_2.add(s1[i])
                c+=1
        if c>2:
            return False
        if set_1 != set_2:
            return False
        return True