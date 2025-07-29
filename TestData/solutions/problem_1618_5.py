class Solution:
    def solution_1618_5(self, arr: List[int]) -> int:
        arr_dict = defaultdict(int)
        ans = -1
        for num in arr:
            num_sum = sum(int(num) for num in str(num))
            if num_sum in arr_dict:
                ans = max(ans, num + arr_dict[num_sum])
            arr_dict[num_sum] = max(arr_dict[num_sum], num)

        return ans