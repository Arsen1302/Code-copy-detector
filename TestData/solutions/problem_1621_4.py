class Solution:
    def solution_1621_4(self, ranks: List[int], suits: List[str]) -> str:
        N = len(ranks)
        statistic = defaultdict(int)

        letter_freq = Counter(suits).most_common(1)
        number_freq = Counter(ranks).most_common(1)
        
        if letter_freq[0][1] >=5:
            return "Flush"

        if number_freq[0][1] >=3:
            return "Three of a Kind"
        if number_freq[0][1] >= 2:
            return "Pair"

        return "High Card"