class Solution:
    def solution_1704_2(self, nums, space):
        dict1 = defaultdict(int)

        for i in nums:
            dict1[i%space] += 1

        max_val = max(dict1.values())

        return min([i for i in nums if dict1[i%space] == max_val])