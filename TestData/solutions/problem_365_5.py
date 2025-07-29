class Solution:
    def solution_365_5(self, nums):
        heap = [(k[0], 0, i) for i, k in enumerate(nums)]
        heapq.heapify(heap)   
        cmax = max(k[0] for k in nums)
        ans = (heap[0][0], cmax)
        while len(nums[heap[0][2]]) != heap[0][1] + 1:
            val, index, row = heapq.heappop(heap)
            cmax = max(cmax, nums[row][index + 1])
            heapq.heappush(heap, (nums[row][index + 1], index + 1, row))
            if cmax - heap[0][0] < ans[1] - ans[0]:
                ans = (heap[0][0], cmax)
        return ans