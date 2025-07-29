class Solution:
    def solution_948_1(self, s: str) -> str:
        nums, chars = [], []
        [(chars, nums)[char.isdigit()].append(str(char)) for char in s]
        nums_len, chars_len = len(nums), len(chars)
        if 2 > nums_len - chars_len > -2:
            a, b = ((chars, nums), (nums, chars))[nums_len > chars_len]
            return reduce(lambda x, y: x + y[0] + y[1], itertools.zip_longest(a, b, fillvalue=''), '')
        return ''