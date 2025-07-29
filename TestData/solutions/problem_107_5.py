class Solution:
    def solution_107_5(self, nums: List[int], k: int, t: int) -> bool:
        if not nums or t < 0: return False
        min_val = min(nums)
        bucket_key = lambda x: (x-min_val) // (t+1)       # A lambda function generate buckey key given a value
        d = collections.defaultdict(lambda: sys.maxsize)  # A bucket simulated with defaultdict
        for i, num in enumerate(nums):
            key = bucket_key(num)                         # key for current number `num`
            for nei in [d[key-1], d[key], d[key+1]]:      # check left bucket, current bucket and right bucket
                if abs(nei - num) <= t: return True
            d[key] = num    
            if i >= k: d.pop(bucket_key(nums[i-k]))       # maintain a size of `k` 
        return False