class Solution:
    # Extremely Fast O(K * N * logN) Solution k -> Maximum Digits, n -> numbers in nums
    # Prepare a defaultdict cache for each trim length
    # Since each num is given as a string you can slice the string till trim from last
    # Now store this sliced string with the original index of it in nums
    # Sort this list using sort of python (nlogn)
    # Append the result to the res
    
    def solution_1619_5(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        
        trim_length_cache = defaultdict(list)
        res = [0] * len(queries)
        for i, (k, trim) in enumerate(queries):
            if trim not in trim_length_cache:
                trim_length_cache[trim] = [(num[-trim:], index) for index, num in enumerate(nums)]
                trim_length_cache[trim].sort()
            res[i] = trim_length_cache[trim][k - 1][1]
        return res