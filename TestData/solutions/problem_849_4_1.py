class Solution:
    def solution_849_4_1(self, nums: List[int], k: int) -> bool:
        
        def solution_849_4_2(num_counts, val, left):
            if left == 0:
                return True
            if val not in num_counts:
                return False
            else:
                num_counts[val] -= 1
                if num_counts[val] == 0:
                    del(num_counts[val])
            return solution_849_4_2(num_counts, val+1, left-1)
        
        if (len(nums) % k != 0):
            return False
        rounds = len(nums) // k
        num_counts = collections.Counter(nums)
        for _ in range(rounds):
            start = min(num_counts.keys())
            #print("start: ", start)
            if not solution_849_4_2(num_counts, start, k):
                #print("failing", start, num_counts)
                return False
        return True