class Solution:
    def solution_1225_5(self, orders: List[List[int]]) -> int:
        buy_log = []
        sell_log = []
        for price, amount, order_type in orders:
            if order_type:
                while buy_log and amount:
                    buy_price, buy_amount = heappop(buy_log)
                    if -buy_price >= price:
                        if buy_amount <= amount:
                            amount -= buy_amount
                        else:
                            buy_amount -= amount
                            heappush(buy_log, (buy_price, buy_amount))
                            amount = 0
                    else:
                        heappush(buy_log, (buy_price, buy_amount))
                        break
                if amount:
                    heappush(sell_log, (price, amount))
            else:
                while sell_log and amount:
                    sell_price, sell_amount = heappop(sell_log)
                    if sell_price <= price:
                        if sell_amount <= amount:
                            amount -= sell_amount
                        else:
                            sell_amount -= amount
                            heappush(sell_log, (sell_price, sell_amount))
                            amount = 0
                    else:
                        heappush(sell_log, (sell_price, sell_amount))
                        break
                if amount:
                    heappush(buy_log, (-price, amount))
        return (sum(amount for _, amount in buy_log) +
                sum(amount for _, amount in sell_log)) % 1_000_000_007