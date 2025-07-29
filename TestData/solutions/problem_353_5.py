class Solution:
    def solution_353_5(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        min_ind_sum = -1
        if len(list1) < len(list2):
            for i in range(len(list1)):
                if list1[i] in list2:
                    ind_sum = i + list2.index(list1[i])
                    if min_ind_sum == -1 or ind_sum < min_ind_sum:
                        res.clear()
                        res.append(list1[i])
                        min_ind_sum = ind_sum
                    elif ind_sum == min_ind_sum:
                        res.append(list1[i])
        else:
            for i in range(len(list2)):
                if list2[i] in list1:
                    ind_sum = i + list1.index(list2[i])
                    if min_ind_sum == -1 or ind_sum < min_ind_sum:
                        res.clear()
                        res.append(list2[i])
                        min_ind_sum = ind_sum
                    elif ind_sum == min_ind_sum:
                        res.append(list2[i])
        return res