class Solution:
    def solution_950_5(self, croakOfFrogs: str) -> int:
        counter = defaultdict(int)
        counter[''] = sys.maxsize
        mapping = {'c': '', 'r': 'c', 'o': 'r', 'a': 'o', 'k': 'a'}

        res = current = 0

        for char in croakOfFrogs:
            counter[char] += 1
            if counter[char] > counter[mapping[char]]:
                return -1

            if char == 'c':
                current += 1
            elif char == 'k':
                current -= 1

            res = max(res, current)
        
        if counter['c'] != counter['k']:
            return -1
            
        return res