class Solution:
    def solution_1150_2(self, customers: List[List[int]]) -> float:
        waits_total = 0
        end_prev_order = customers[0][0]
        
        for arrival, time in customers:
            overhead = end_prev_order - arrival if end_prev_order > arrival else 0
            waits_total += time + overhead
            end_prev_order = max(end_prev_order, arrival) + time 

        return waits_total / len(customers)