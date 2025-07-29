class Solution:
    def solution_949_2(self, orders: List[List[str]]) -> List[List[str]]:
        freq = {} 
        foods = set()
        
        for _, table, food in orders: 
            freq.setdefault(table, defaultdict(int))[food] += 1
            foods.add(food)
        
        foods = sorted(foods)
        ans = [["Table"] + foods]
        for k in sorted(freq, key=int): 
            row = [k]
            for food in foods: 
                row.append(str(freq[k][food]))
            ans.append(row)
        return ans