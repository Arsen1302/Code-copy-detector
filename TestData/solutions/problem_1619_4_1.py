class Solution:
    # Radix Sort Solution
    # MAKE a mapper for the queries
    # Write the good old count sort algorithm
    # For each time you go over a placeval iteration for the radix sort
    # Check if that iteration/trim is present in the mapper you made earlier
    # If yes then for that query item update the res
    # Edge case is when the new sorted array is same as the OG given nums
    # This could also mean that there are some repeated elements
    # So instead offinding the index in the OG nums just update res with the position asked
    # as that will be the answer for that query
    def solution_1619_4_1(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        def solution_1619_4_2(placeval, k = 10):
            counts = [0] * k
            
            for elem in nums:
                digit = (elem // placeval) % 10
                counts[digit] += 1
            s = 0
            for i, count in enumerate(counts):
                counts[i] = s
                s += count
            sorted_list = [0] * len(nums)
            for elem in nums:
                digit = (elem // placeval) % 10
                sorted_list[counts[digit]] = elem
                counts[digit] += 1
            nums[:] = list(sorted_list)
        mapper = defaultdict(list)
        for i, (k, trim) in enumerate(queries):
            mapper[trim].append((k, i))
        nums[:] = [int(num) for num in nums]
        og = list(nums)
        #Radix sort starts
        maxi = max(nums)
        res = [0] * len(queries)
        placeval, trim = 1, 1
        while placeval <= maxi:
            solution_1619_4_2(placeval)
            if trim in mapper:
                for k, pos in mapper[trim]:
                    if nums == og: res[pos] = k - 1
                    else: res[pos] = og.index(nums[k - 1])
            placeval *= 10
            trim += 1
        return res