class Solution:
    def solution_736_4(self, text: str, first: str, second: str) -> List[str]:
        word_list = text.split()
        return [word_list[sec+1] for sec, word in enumerate(word_list[:-2], 1) if word == first and word_list[sec] == second]