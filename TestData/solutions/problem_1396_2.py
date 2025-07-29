class Solution:
    def solution_1396_2(self, s):
        nums = re.findall(r'\d+', s)
        return nums == sorted(set(nums), key=int)