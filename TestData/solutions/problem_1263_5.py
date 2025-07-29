class Solution:
    def solution_1263_5(self, nums: List[int]) -> int:
        
        N, maximum = len(nums), 0
        cumulative, stack = [0], []
        for num in nums:
            cumulative.append(cumulative[-1] + num)
            
        for i, num in enumerate(nums + [-float(inf)]):
            start = i
            while stack and stack[-1][1] > num:
                index, value = stack.pop()
                total = cumulative[i] - cumulative[index]
                maximum = max(value * total, maximum)
                start = index
            stack.append((start, num))
            
        return maximum % (10**9 + 7)