class Solution:
    def solution_1225_4(self, orders: List[List[int]]) -> int:
        backlog = ([], [])  # (buy (max-heap), sell (min-heap))
        for price, amount, order_type in orders:
            # check that the appropriate buy/sell order fits the criteria in the while loop
            # note that le, ge come from the Python operator library
            # equivalent to: le - lambda a, b: a <= b
            #                ge - lambda a, b: a >= b
            while amount > 0 and \
                    (target_log := backlog[1-order_type]) and \
                    (le, ge)[order_type](abs(target_log[0][0]), price):
                curr_price, curr_amount = heappop(target_log)
                if (amount := amount-curr_amount) < 0:  # there are remaining target orders
                    heappush(target_log, (curr_price, -amount))
            if amount > 0:  # there are remaining current orders
                heappush(backlog[order_type], (price if order_type else -price, amount))
        # note that itemgetter comes from the Python operator library
        # equivalent to: lambda t: t[1]
        return sum(sum(map(itemgetter(1), log)) for log in backlog)%int(1e9+7)