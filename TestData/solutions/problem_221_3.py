class Solution:
    def solution_221_3(self, n: int) -> List[str]:
        a=1
        b=1
        l=[]
        for i in range(1,n+1):
            if a==3 and b==5:
                l.append('FizzBuzz')
                a=1
                b=1
            elif b==5:
                l.append('Buzz')
                b=1
                a=a+1
            elif a==3:
                l.append('Fizz')
                a=1
                b=b+1
            else:
                l.append(str(i))
                a=a+1
                b=b+1
        return l