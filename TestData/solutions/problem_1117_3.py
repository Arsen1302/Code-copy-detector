class Solution1:
    def solution_1117_3(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        """Very difficult one. I had the intuition correct, that by using BFS,
        we can always find the solution when x is reachable. The difficulty is
        when x is not reachable. Since we can always add a, there is no end
        to BFS. Thus, the key to the problem is to find the upper bound for
        BFS. If no solution is found within the upper bound, we can say x is
        not reachable.

        To determine the upper bound, we have to use the Bezout's Identity,
        which stipulates that given any integers u and v, a * v + b * v = n *
        gcd(a, b). In addition, we need some ingenuity, which is detailed in
        this post: https://leetcode.com/problems/minimum-jumps-to-reach-home/discuss/978357/C%2B%2B-bidirectional-BFS-solution-with-proof-for-search-upper-bound

        I am going to describe here my understanding of finding the upper bound.

        We know that if a >= b, we basically cannot go left. Thus, the upper
        bound is x itself. This means if we go beyond x, there is no way we
        can go back. So whenever we go beyond x, we know x is not reachable.

        If a < b, we can go right and left. Now we can definitely go beyond x.
        Furthermore, to verify all possibilities, we have to go beyond
        max(forbidden), because the forbidden values add another layer of
        complexity. We must go beyond that to hit all possibilities associated
        with the forbidden value. Thus, the upper bound must be beyond max(x,
        max(forbidden)).

        Given Bezout's Identity, let p = n * gcd(a, b) that is the smallest
        value bigger than max(x, max(forbidden)). p is the left most point that
        we can reach beyond max(x, max(forbidden)). Notice that there is no
        more forbidden value to the right of p. Therefore, we don't have to
        worry about the added complexity of forbidden values now.

        Let's say we are at p right now. The first move we can make that will
        land us in the new territory is p + a. Since a is a multiple of
        gcd(a, b), there are other points we can reach between p and p + a,
        such as:

        p + gcd(a, b), p + 2 * gcd(a, b), ..., p - gcd(a, b) + a

        Note that all these positions can only be reached by a left jump.
        Therefore, the upper bound must be p - gcd(a, b) + a + b.

        One might ask, why can't we go beyond p - gcd(a, b) + a + b? We
        certainly can, but going beyond p - gcd(a, b) + a + b won't help us to
        reach x if we don't go left. And if we go left, eventually we will end
        up at one of the positions in [p, p + a] again, and when that happens,
        we have already taken more steps than visiting the positions in
        [p, p + a] for the first time.

        Therefore, the upper bound must be p - gcd(a, b) + a + b.

        Since p = n * gcd(a, b) is the smallest multiple of gcd(a, b) that is
        larger than max(x, max(forbidden)), we have
        p - gcd(a, b) <= max(x, max(forbidden)). Thus, p - gcd(a, b) + a + b <=
        max(x, max(forbidden)) + a + b.

        Therefore, it is perfectly okay for us to set the upper bound to be
        max(x, max(forbidden)) + a + b

        Once we have the upper bound, we can use BFS to find the solution.

        O(max(x, max(forbidden)) + a + b), 264 ms, faster than 31.58%
        """
        upper_bound = max(x, max(forbidden)) + a + b
        forbidden = set(forbidden)
        queue = set([(0, False)])
        steps = 0
        visited = set()
        while queue:
            temp = set()
            for pos, is_pre_left in queue:
                visited.add(pos)
                if pos == x:
                    return steps
                if pos + a <= upper_bound and pos + a not in forbidden and pos + a not in visited:
                    temp.add((pos + a, False))
                if pos - b >= 0 and pos - b not in forbidden and pos - b not in visited and not is_pre_left:
                    temp.add((pos - b, True))
            if temp:
                steps += 1
            queue = temp
        return -1