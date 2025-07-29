class Solution:
    # observe : if there are an even number of negatives, we can get rid of them all! just bubble the negatives towards each other... and pairwise become positive
    # if there's an odd number, we greedily pairwise the largest negatives in abs value. The remaining negative, we can actually transfer into the smallest absolute value... In the case of a 0, we can transfer the last negative into the 0.

    # O(n^2) time : O(1) space
    def solution_1349_3(self, matrix: List[List[int]]) -> int:
        n, count_neg, abs_sum, min_abs = len(matrix), 0, 0, float('inf')
        for i in range(n):
            for j in range(n):
                count_neg += matrix[i][j] < 0
                abs_sum += abs(matrix[i][j])
                min_abs = min(min_abs, abs(matrix[i][j]))
        return abs_sum if count_neg % 2 == 0 else abs_sum - 2 * min_abs