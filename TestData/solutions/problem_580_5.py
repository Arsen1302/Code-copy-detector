class Solution:
    def solution_580_5(self, words: List[str]) -> int:
        for i in range(len(words)):
            even = []
            odd = []
            word = words[i]
            for j in range(len(word)):
                if j%2 == 0:
                    even.append(word[j])
                else:
                    odd.append(word[j])
            even.sort()
            odd.sort()
            words[i] = ''.join(even) + ''.join(odd)
        return len(set(words))