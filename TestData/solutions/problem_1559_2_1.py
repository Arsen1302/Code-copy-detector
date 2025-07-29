class Solution:
    def solution_1559_2_1(self, nums: List[int], k: int, p: int) -> int:
        def solution_1559_2_2(idx, k, path):
            nonlocal res, visited
            if idx == len(nums):
                visited.add(tuple(path[:]))
                return
            
            if nums[idx] % p == 0 and k > 0:
                path.append(nums[idx])
                if tuple(path) not in visited:
                    visited.add(tuple(path))
                    res += 1
                solution_1559_2_2(idx + 1, k - 1, path)
            elif nums[idx] % p != 0:
                path.append(nums[idx])
                if tuple(path) not in visited:
                    visited.add(tuple(path))
                    res += 1
                solution_1559_2_2(idx + 1, k, path)
            
        res = 0
        visited = set()
        for i in range(len(nums)):
            solution_1559_2_2(i, k, [])
        return res