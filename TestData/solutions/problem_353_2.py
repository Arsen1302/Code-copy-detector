class Solution:
    def solution_353_2(self, list1: List[str], list2: List[str]) -> List[str]:
        list3 = set(list1) &amp; set(list2)
        m, v = 3000, []
        for i in list3:
            s = list1.index(i) + list2.index(i)
            if m > s:
                v = [i]
                m = s
            elif m == s:
                v.append(i)
        return v