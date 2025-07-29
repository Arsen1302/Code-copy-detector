class Solution:
    def solution_949_3(self, orders: List[List[str]]) -> List[List[str]]:
        
        category={}
        foods=['Table']
        for order in orders:
            if order[1] not in category.keys():
                category[order[1]]={}
            if order[2] not in category[order[1]].keys():
                category[order[1]][order[2]]=1
            else:
                category[order[1]][order[2]]+=1
            if order[2] not in foods:
                foods.append(order[2])

        tables = category.keys()
        foods = [foods[0]]+sorted(foods[1:])
        ans=[foods]
        
        for k in sorted(category.keys(),key=int):
            table=[]
            table.append(str(k))
            for i in range(1,len(foods)):
                if foods[i] in category[k].keys():
                    table.append(str(category[k][foods[i]]))
                else:
                    table.append('0')
            ans+=[table]
        return ans