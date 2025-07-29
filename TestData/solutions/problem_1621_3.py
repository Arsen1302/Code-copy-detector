class Solution:
    def solution_1621_3(self, ranks: List[int], suits: List[str]) -> str:
        N = len(ranks)
        statistic = defaultdict(int)

        letter_freq = 0
        number_freq = 0

        for i in range(N):
            statistic[ranks[i]] += 1
            statistic[suits[i]] += 1
            letter_freq = max(letter_freq, statistic[suits[i]])
            number_freq = max(number_freq, statistic[ranks[i]])

        if letter_freq >=5:
            return "Flush"

        if number_freq >=3:
            return "Three of a Kind"
        if number_freq >= 2:
            return "Pair"

        return "High Card"