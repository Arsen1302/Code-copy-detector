class Solution:
    def solution_476_3(self, arr: List[int], k: int) -> List[int]:
        '''
        I want to go from Input: arr = [1,2,3,5], k = 3 ; Output: [2,5]
        
        Each [(num1, num2, fraction), ...]
        To: [(1, 5, 1/5), (1, 3, 1/3), (2, 5, 2/5), (1, 2, 1/2), (3, 5, 3/5), (2, 3, 2/3)]
                                        ^^^^^^^^^
        after sorting by fraction ASC
        and return the [num1, num2] of the kth-smallest fraction -> [2, 5] from (2, 5, 2/5)
        '''
        N, data = len(arr), []
        
        # Collect the data in the target data structure
        for one in range(N - 1):
            for two in range(one + 1, N):
                data.append((arr[one], arr[two], arr[one] / arr[two]))
                
        # Sort the data based on logic pre-defined above -> sorting on fraction ASC
        data.sort(key=lambda x: x[2])
        
        # Return k-th data in required format, [num_one, num_two]
        kth_data = data[k - 1]
        num_one, num_two, fraction = kth_data
        return [num_one, num_two]