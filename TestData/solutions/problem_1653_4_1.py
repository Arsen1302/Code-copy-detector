class Solution:
    def solution_1653_4_1(self, garbage: List[str], travel: List[int]) -> int:
        m = p = g = -1
        self.time = 0
        T = [0]
        for t in travel: T.append(t)
        
        for i, house in enumerate(garbage):
            if 'M' in house: m = i
            if 'P' in house: p = i
            if 'G' in house: g = i
                
        def solution_1653_4_2(type, x):
            for i, house in enumerate(garbage):
                if i > x: break
                self.time += T[i]
                if type in house: self.time += house.count(type)
        
        solution_1653_4_2('M', m)
        solution_1653_4_2('P', p)
        solution_1653_4_2('G', g)
        
        return self.time