class Solution:
    def solution_1225_3(self, orders: List[List[int]]) -> int:
        # note that: buy_log - max heap; sell_log - min heap
        buy_log, sell_log = [], []
        for price, amount, order_type in orders:
            target_log = buy_log if order_type else sell_log
            while amount and target_log:
                # check that the appropriate buy/sell order fits the criteria
                # if order type is sell, ensure buy order price >= current price
                # else if order type is buy, ensure sell order price <= current price
                if (order_type and abs(target_log[0][0]) < price) or \
                        (not order_type and target_log[0][0] > price):
                    break
                current_price, current_amount = heappop(target_log)
                # cancel buy and sell orders
                min_amount = min(amount, current_amount)
                amount -= min_amount
                current_amount -= min_amount
                # check if there are remaining target orders
                if current_amount:
                    heappush(target_log, (current_price, current_amount))
            # check if there are remaining current orders
            if amount:
                heappush(sell_log if order_type else buy_log,
                         # negate price if order type is buy
                         # so as to maintain a max heap for buy orders
                         (price if order_type else -price, amount))
        return (sum(log_amount for _, log_amount in buy_log) + \
                sum(log_amount for _, log_amount in sell_log))%int(1e9+7)