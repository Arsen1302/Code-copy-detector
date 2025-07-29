class Solution:
    def solution_353_3(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        min_index = 10**4
        for i in set(list1).intersection(set(list2)):
            z = list1.index(i) + list2.index(i)
            if min_index > z:
                min_index = z
                ans = [i]
            elif min_index == z:
                ans.append(i)
        return ans