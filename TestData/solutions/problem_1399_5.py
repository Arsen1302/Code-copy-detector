class Solution:
    def solution_1399_5(self, sentence: str) -> int:
        pattern = re.compile(r'(^[a-z]+(-[a-z]+)?)?[,.!]?$')
        count = 0
        
        for token in sentence.split():
            if pattern.match(token):
                count += 1
                
        return count