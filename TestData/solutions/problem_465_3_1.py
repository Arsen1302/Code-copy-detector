class Solution:
    def solution_465_3_1(self, board: List[List[int]]) -> int:
        
        heap = []
        board = tuple(num for row in board for num in row)
        heap.append((0, board))
        heapq.heapify(heap)
        
        visited = set()
        visited.add(board)
        
        def solution_465_3_2(nums):
            a, b, c, d, e, f = nums
            if a == 0:
                return [(b, 0, c, d, e, f), (d, b, c, 0, e, f)]
            elif b == 0:
                return [(0, a, c, d, e, f), (a, c, 0, d, e, f), (a, e, c, d, 0, f)]
            elif c == 0:
                return [(a, 0, b, d, e, f), (a, b, f, d, e, 0)]
            elif d == 0:
                return [(0, b, c, a, e, f), (a, b, c, e, 0, f)]
            elif e == 0:
                return [(a, b, c, 0, d, f), (a, b, c, d, f, 0), (a, 0, c, d, b, f)]
            elif f == 0:
                return [(a, b, c, d, 0, e), (a, b, 0, d, e, c)]
        
        while heap:
            cost, nums = heapq.heappop(heap)
            if tuple([num for num in nums]) == (1, 2, 3, 4, 5, 0):
                return cost
            else:
                for neighbor in solution_465_3_2(nums):
                    if neighbor not in visited:
                        heapq.heappush(heap, (cost + 1, neighbor))
                        visited.add(neighbor)
        
        return -1