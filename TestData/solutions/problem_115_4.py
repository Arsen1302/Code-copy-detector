class Solution:
    def solution_115_4(self, nums: List[int]) -> List[int]:
        decider = len((nums))//3
        d = {}
        op = []
        for x in nums:
          if x not in d:
            d[x] = 1
          else:
            d[x] += 1
        for x, y in d.items():
          if y > decider:
            op.append(x)
        return op