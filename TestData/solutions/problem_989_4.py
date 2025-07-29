class Solution:
    def solution_989_4(self, arr: List[int], k: int) -> List[int]:
        arr, arr_len = sorted(arr), len(arr)
        m = arr[int((arr_len-1)/2)]
        # Pickup top k tuple
        # arr = [1,2,3,4,5] -> ss_list = [(2, 5), (2, 1), (1, 4), (1, 2), (0, 3)]
        #                      ss_list[:k] = [(2, 5), (2, 1)]
        ss_list = list(sorted(map(lambda e: (abs(e-m), e), arr), reverse=True))[:k]
        
        # Pickup the element
        # ss_list -> [5, 1]
        ss_list = list(map(lambda t: t[1], ss_list))
        return ss_list