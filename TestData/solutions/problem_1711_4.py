class Solution:
    def solution_1711_4(self, nums: List[int], k: int) -> int:
        seen = collections.defaultdict(int)
        s = 0
        res = 0
        for i in range(k):
            s += nums[i]
            seen[nums[i]] += 1
        if len(seen) == k:
            res = s
        for i in range(k, len(nums)):
            s -= nums[i - k]
            s += nums[i]
            seen[nums[i - k]] -= 1
            if seen[nums[i - k]] == 0:
                del seen[nums[i - k]]
            seen[nums[i]] += 1
            if len(seen) == k:
                res = max(res, s)
        return res

class Solution {
    public long solution_1711_4(int[] nums, int k) {
        Map<Integer, Integer> seen = new HashMap<>();
        long s = 0;
        long res = 0;
        for (int i = 0; i < k; i ++) {
            s += (long)nums[i];
            seen.put(nums[i], seen.getOrDefault(nums[i], 0) + 1);
        }
        if (seen.size() == k) {
            res = s;
        }
        for (int i = k; i < nums.length; i ++) {
            s -= nums[i - k];
            s += nums[i];
            seen.put(nums[i - k], seen.get(nums[i - k]) - 1);
            if (seen.get(nums[i - k]) == 0) {
                seen.remove(nums[i - k]);
            }
            seen.put(nums[i], seen.getOrDefault(nums[i], 0) + 1);
            if (seen.size() == k) {
                res = Math.max(res, s);
            }
        }
        return res;
    }
}