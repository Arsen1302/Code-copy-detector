class Solution:
    def solution_1179_4_1(self, arr, k, low, high):
        """
        select k largest element
        """
        def solution_1179_4_2(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        def solution_1179_4_3(arr, low, high):
            """
            select last elem as pivot, return the pivot index after rearranged array
            """
            # randomly choose index
            randidx = random.randint(low,high)
            pivot = arr[randidx]
            solution_1179_4_2(arr, randidx, high)

            i = low
            for j in range(low, high):
                if arr[j] > pivot:
                    solution_1179_4_2(arr, i, j)
                    i += 1

            solution_1179_4_2(arr, i, high)
            return i
        
        if low == high:
            return arr[low]

        pivot_idx = solution_1179_4_3(arr, low, high)

        if k-1 == pivot_idx:
            return arr[pivot_idx]
        elif k-1 > pivot_idx: 
            return self.solution_1179_4_1(arr, k, pivot_idx+1, high)
        else:
            return self.solution_1179_4_1(arr, k, low, pivot_idx-1)

        return solution_1179_4_1(nums, k, 0, len(nums)-1)
    
    def solution_1179_4_4(self, matrix: List[List[int]], k: int) -> int:
        """
        prefix-XOR
        flatten matrix into 1d
        solution_1179_4_1(k)
        [ ][-][+][ ]
        [ ][+][x][ ]
        [ ][ ][ ][ ]
        [ ][ ][ ][ ]
        """
        nrow, ncol = len(matrix), len(matrix[0])
        prefix_XOR = [[0 for _ in range(ncol)] for _ in range(nrow)] 
        
        # init first row and first col
        prefix_XOR[0][0] = matrix[0][0]
        for i in range(1,ncol):
            prefix_XOR[0][i] = prefix_XOR[0][i-1] ^ matrix[0][i]
        for i in range(1,nrow):
            prefix_XOR[i][0] = prefix_XOR[i-1][0] ^ matrix[i][0]
        # prefix XOR
        for i in range(1,nrow):
            for j in range(1,ncol):
                prefix_XOR[i][j] = matrix[i][j] ^ prefix_XOR[i-1][j] ^ prefix_XOR[i][j-1] ^ prefix_XOR[i-1][j-1]
                
        # flatten 2d matrix into 1d
        flatten = []
        for i in prefix_XOR:
            flatten += i
            
        # quick select k
        # res = self.solution_1179_4_1(flatten, k, 0, len(flatten)-1) # why solution_1179_4_1 not working? (TLE)
        res = sorted(flatten)[-k] # why built-in sorted() works?
        
        return res