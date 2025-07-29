class Solution:
    def solution_365_3(self, nums: List[List[int]]) -> List[int]:
        
        curr_v = [(l[0], i, 0) for i, l in enumerate(nums)]
        heapq.heapify(curr_v)
        currmax = max(curr_v)[0]

        minrange = currmax - curr_v[0][0]
        minrange_value = [curr_v[0][0], currmax]

        while curr_v[0][2] < len(nums[curr_v[0][1]]) - 1:
            # print(curr_v)
            _, r_idx, c_idx = heapq.heappop(curr_v)
            newentry = (nums[r_idx][c_idx + 1], r_idx, c_idx + 1)
            heapq.heappush(curr_v, newentry)
            if newentry[0] > currmax:
                currmax = newentry[0]
            if currmax - curr_v[0][0] < minrange:
                minrange = currmax - curr_v[0][0]
                minrange_value = [curr_v[0][0], currmax]

        return minrange_value