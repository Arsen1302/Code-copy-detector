class Solution:
    def solution_376_5(self, dictionary: List[str], sentence: str) -> str:
        sen = sentence.split(' ')
        dic = sorted(dictionary)
        for i, word in enumerate(sen):
            for root in dic:
                if word[:len(root)] == root:
                    sen[i] = root
                    break
        return ' '.join(sen)