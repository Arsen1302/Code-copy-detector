class Solution:
    def solution_935_4(self, satisfaction: List[int]) -> int:
        if max(satisfaction) <= 0 : return(0)
        # elif min(satisfaction) >= 0 : return(satisfaction.sort())

        s_sorted = satisfaction.copy()
        s_sorted.sort()
        i_positive = 0
        print(s_sorted)
        for i in s_sorted:
            if i >= 0: break
            else:
                i_positive = i_positive + 1
        print(i_positive)
        max_sum = 0

        len_negative = len(s_sorted[:i_positive])
        for i in range(len_negative+1):
            temp = 0
            k = 1
            for j in s_sorted[i_positive-i:]:
                temp = temp + j*k
                k = k + 1
            if max_sum<temp: max_sum = temp
        return(max_sum)