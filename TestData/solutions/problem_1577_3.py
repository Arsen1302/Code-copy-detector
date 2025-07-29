class Solution:
    def solution_1577_3(self, messages: List[str], senders: List[str]) -> str:
        word_count = {}
        
        for message, sender in zip(messages, senders):
            message_word_count = message.count(" ") + 1
            word_count[sender] = word_count.get(sender, 0) + message_word_count
            
        top_sender = ""
        max_count = 0
        
        for sender, wc in word_count.items():
            if wc > max_count or (wc == max_count and sender > top_sender ):
                top_sender = sender
                max_count = wc
                
        return top_sender