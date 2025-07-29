class Solution:
    def solution_353_1(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        d2 = {}
        min_ = 5000
        ret = []

        for i in range(len(list1)):
            d[list1[i]] = i+1

        for i in range(len(list2)):
            a = d.get(list2[i], 0)
            if a:
                b = a+i-1
                if b <= min_:
                    min_ = b
                    d2[list2[i]] = b

        for k,v in d2.items():
            if v <= min_:
                ret.append(k)

        return ret