class Solution:
  def solution_1619_1_1(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        def solution_1619_1_2(indices, pos):
            count = [0] * 10
            for idx in indices:
                count[ord(nums[idx][pos]) - ord('0')] += 1
            start_pos = list(accumulate([0] + count, add))
            result = [None] * len(indices)
            for idx in indices:
                digit = ord(nums[idx][pos]) - ord('0')
                result[start_pos[digit]] = idx
                start_pos[digit] += 1
            return result
            
        n = len(nums)
        m = len(nums[0])
        suffix_ordered = [list(range(n))]
        for i in range(m - 1, -1, -1):
            suffix_ordered.append(solution_1619_1_2(suffix_ordered[-1], i))
        return [suffix_ordered[t][k-1] for k, t in queries]