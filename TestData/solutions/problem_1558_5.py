class Solution:
    def solution_1558_5(self, cards: List[int]) -> int:
        cards_dict = defaultdict(list)
        ans = float("inf")
        for i in range(len(cards)):
            cards_dict[cards[i]].append(i)

        for key in cards_dict:
            arr = cards_dict[key]
            for j in range(len(arr) - 1):
                ans = min(ans, (arr[j + 1] - arr[j] + 1))
        return ans if ans < float("inf") else -1