class Solution:
    def solution_1617_4(self, nums: List[int]) -> List[int]:
        dict_numbers = {}
        for i in nums:
            if i not in dict_numbers:
                dict_numbers[i] = 1
            else:
                dict_numbers[i] += 1

        count_pairs = 0
        count_leftovers = 0
        result = []
        for k, v in dict_numbers.items():

            if v % 2 != 0:
                count_pairs += v // 2
                count_leftovers += v % 2
            else:
                count_pairs += v // 2
        result.append(count_pairs)
        result.append(count_leftovers)
        return result