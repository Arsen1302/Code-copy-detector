class Solution:
    def solution_1577_2(self, messages: List[str], senders: List[str]) -> str:
        words_count = defaultdict(int)
        for m, person in zip(messages, senders):
            words_count[person] += len(m.split())
                
        max_len = max(words_count.values())
        
        names = sorted([name for name, words in words_count.items() if words == max_len], reverse=True)
        return names[0]