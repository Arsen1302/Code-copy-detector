class Solution:
    def solution_640_5_1(self, grid: List[str]) -> int:
        n,m=len(grid),len(grid[0])
        parent=[i for i in range((n+1)*(m+1))]
        rank=[1 for i in range((n+1)*(m+1))]
        matrix=[]
        cc=0
        for i in range(n+1):
            li=[]
            for j in range(m+1):
                li.append(cc)
                cc+=1
            matrix.append(li)
        boundary=[]
        boundary+=matrix[0]
        for row in range(1,len(matrix)-1):
            li=[matrix[row][0],matrix[row][-1]]
            boundary+=li
        boundary+=matrix[-1]
        boundary=boundary[1:]
        def solution_640_5_2(x):
            if parent[x]==x:
                return x
            temp=solution_640_5_2(parent[x])
            parent[x]=temp
            return temp
        def solution_640_5_3(x,y):
            parentx=solution_640_5_2(x)
            parenty=solution_640_5_2(y)
            if parentx!=parenty:
                if rank[parentx]<rank[parenty]:
                    parent[parentx]=parenty
                elif rank[parentx]>rank[parenty]:
                    parent[parenty]=parentx
                else:
                    parent[parentx]=parenty
                    rank[parenty]+=1
        for b in boundary:
            solution_640_5_3(0,b)
        count=1
        for row in range(n):
            for col in range(m):
                if grid[row][col]==" ":
                    continue
                elif grid[row][col]=="\\":
                    point1=row*(m+1)+col
                    point2=(row+1)*(m+1)+(col+1)
                else:
                    point1=((row+1)*(m+1))+(col)
                    point2=(row*(m+1))+(col+1)
                pp1=solution_640_5_2(point1)
                pp2=solution_640_5_2(point2)
                solution_640_5_3(point1,point2)
                if pp1==pp2:
                    count+=1
        return count