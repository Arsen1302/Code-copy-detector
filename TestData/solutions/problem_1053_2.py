class Solution:
    def solution_1053_2(self, n: int, rounds: List[int]) -> List[int]:
        # count the length of distance starting from rounds[0]:
		distance = 1
        for i in range(1, len(rounds)):
            if rounds[i - 1] < rounds[i]:
                distance += rounds[i] - rounds[i - 1]
            
            else:
                distance += n - (rounds[i - 1] - rounds[i])
        
		# mapping= {number: frequency}
        mapping = collections.defaultdict(int)
        # be careful that the iteration should start from rounds[0]
        for i in range(rounds[0], rounds[0] + distance):
            if i % n != 0:
                mapping[i % n] += 1
            
            else:
                mapping[n] += 1
         
		 # find out the most frequent numbers
        maxFreq = max(mapping.values())

        res = []
        
        for key in mapping:
            if mapping[key] == maxFreq:
                res.append(key)
        
        # sort the result list and retur
        return sorted(res)