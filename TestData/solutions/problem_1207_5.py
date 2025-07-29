class Solution:
    def solution_1207_5(self, nums1: List[int], nums2: List[int]) -> int:
        A, B = nums1, nums2
        sum_a, sum_b = sum(A), sum(B)
        if sum_a > sum_b:
            # keep sum(B) > sum(A)
            A, B = B, A
            sum_a, sum_b = sum_b, sum_a
           
		# get element frequencies
        freq_A, freq_B = [0] * 7, [0] * 7
        for a in A:
            freq_A[a] += 1
        for b in B:
            freq_B[b] += 1
        
        # make sure it's possible
        na, nb = len(A), len(B)
        min_a, max_a = na, 6 * na
        min_b, max_b = nb, 6 * nb
        if min_a > max_b or min_b > max_a:
            return -1
        elif sum_a == sum_b:
            return 0
        
        # get number of equivalent difference-reducing operations available
        num_ops_by_distance = [0] * 6
        for elem in range(1, 7):
            # element A[i] can be increased by up to (6 - A[i])
            num_ops_by_distance[6 - elem] += freq_A[elem]
            # element B[i] can be decreased by up to (B[i] - 1)
            num_ops_by_distance[elem - 1] += freq_B[elem]
            
        diff = sum_b - sum_a
        res = 0
        
        # decrease diff = sum(B) - sum(A) by largest remaining incr/decrements of size delta
        for delta in range(5, 0, -1):
            max_reduction = num_ops_by_distance[delta] * delta
            if diff >= max_reduction:
                # all incr/decrements of size delta are not enough to bridge the remaining difference
                res += num_ops_by_distance[delta]
                diff -= max_reduction
                if diff <= 0:
                    break
            else:
                # get the actual number of operations needed for changes of given size delta
                num_ops_needed, rem = divmod(diff, delta)
                num_ops_needed += (rem > 0)
                res += num_ops_needed
                break
        
        return res