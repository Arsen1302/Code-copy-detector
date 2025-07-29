class Solution:
    def solution_1240_5(self, n: int, k: int) -> int:
        friends = sorted(set(range(1, n + 1)))
        idx = 0
        while len(friends) > 1:
            idx = (idx + k - 1) % len(friends)
            friends.remove(friends[idx])
        return friends[0]