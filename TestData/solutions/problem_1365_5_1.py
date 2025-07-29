class Solution:
    def solution_1365_5_1(self, next_visit: List[int]) -> int:
        p = 10**9 + 7
        n = len(next_visit)
        dp = [0]*n

        for i in range(1,n):
            dp[i] = (2 * dp[i-1] - dp[next_visit[i-1]] + 2) % p

        return dp[-1]

    def solution_1365_5_2(self, next_visit: List[int]) -> int:
        p = 10**9 + 7
        n = len (next_visit)
        not_visited = set(range(n))

        visits = [0] * n
        last_day = [float('-inf')] * n

        def solution_1365_5_3 (room, day):
            not_visited.discard(room)
            while not_visited:
                visits[room] += 1
                last_day[room] = day
                if visits[room] &amp; 1:
                    # This room has been visited an odd number of times.
                    day = (2*day - last_day[next_visit[room]] + 1) % p

                # This room has been visited an even number of times.
                day += 1
                room = (room + 1) % n
                not_visited.discard(room)

            return day

        return solution_1365_5_3 (0, 0) % p