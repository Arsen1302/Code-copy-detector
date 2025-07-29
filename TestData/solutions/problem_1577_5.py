class Solution:
    def solution_1577_5(self, messages: List[str], senders: List[str]) -> str:
        d = defaultdict(int)
        for sender, size in zip( senders, [len(message.split()) for message in messages] ):
            d[sender] += size
        max_word = max(d.values())
        return sorted([sender for sender, size in d.items() if size == max_word])[-1]