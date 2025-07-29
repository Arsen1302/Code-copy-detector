class Solution:
    def solution_691_3_1(self, weights, days):
        min_capacity = max(weights)
        max_capacity = sum(weights)

        def solution_691_3_2(min_capacity, max_capacity, days):
            while min_capacity < max_capacity:
                mid_capacity = (max_capacity + min_capacity) // 2
                curr_days = solution_691_3_3(weights, mid_capacity)

                if curr_days > days:
                    min_capacity = mid_capacity + 1
                else:
                    max_capacity = mid_capacity

            return min_capacity

        def solution_691_3_3(weights, capacity):
            load = 0
            num_days = 1

            for weight in weights:
                if load + weight <= capacity:
                    load += weight
                else:
                    num_days += 1
                    load = weight

            return num_days

        return solution_691_3_2(min_capacity, max_capacity, days)