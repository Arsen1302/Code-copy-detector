class Solution:
    def solution_949_1(self, orders: List[List[str]]) -> List[List[str]]:
                        
        order = defaultdict(lambda : {})
                
        foods = set()
        
        ids = []
        
        for i , t , name in orders:
            t = int(t)
            if(name in order[t]):
                order[t][name] += 1
            else:
                order[t][name] = 1
            if(int(t) not in ids):
                ids.append(int(t))
                
            foods.add(name)
        
        ids.sort()
                        
        foods = list(foods)
        
        foods.sort()
        
        tables = [['Table'] + foods]
        
        k = 0
                
        order = dict(sorted(order.items() , key=lambda x: x[0]))
                
        for _ , j in order.items():
            ans = [str(ids[k])]
            for i in foods:
                if(i in j):
                    ans.append(str(j[i]))
                else:
                    ans.append("0")
            
            tables.append(ans)
            
            k += 1
        
        return tables