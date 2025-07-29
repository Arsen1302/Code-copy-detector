class Solution:
    def solution_1225_1(self, orders: List[List[int]]) -> int:
        ans = 0
        buy, sell = [], [] # max-heap &amp; min-heap 
        
        for p, q, t in orders: 
            ans += q
            if t: # sell order
                while q and buy and -buy[0][0] >= p: # match 
                    pb, qb = heappop(buy)
                    ans -= 2*min(q, qb)
                    if q < qb: 
                        heappush(buy, (pb, qb-q))
                        q = 0 
                    else: q -= qb 
                if q: heappush(sell, (p, q))
            else: # buy order 
                while q and sell and sell[0][0] <= p: # match 
                    ps, qs = heappop(sell)
                    ans -= 2*min(q, qs)
                    if q < qs: 
                        heappush(sell, (ps, qs-q))
                        q = 0 
                    else: q -= qs 
                if q: heappush(buy, (-p, q))
            
        return ans % 1_000_000_007