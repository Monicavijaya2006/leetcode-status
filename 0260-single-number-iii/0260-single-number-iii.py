from math import isqrt

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        '''
            l=[a,a,b,b,c,d,e,e]

            2(a+b+e)+c+d=sum(l)

            2(a+b+e)+c+d+2c-2c+2d-2d=sum(l)

            2(a+b+c+d+e)-(c+d)=sum(l)

            Let,

            S=2*(sum(set(l)))-sum(l)

            S=c+d      ...(1)


            Now, consider the sum of squares:

            a^2+a^2+b^2+b^2+c^2+d^2+e^2+e^2
            = sum(x*x for x in l)

            2(a^2+b^2+e^2)+c^2+d^2
            = sum(x*x for x in l)

            Applying the same manipulation:

            Q=2*(sum(x*x for x in set(l))) - sum(x*x for x in l)

            Q=c^2+d^2      ...(2)

            Using:

            (c+d)^2 = c^2+d^2+2cd

            S^2 = Q+2cd

            cd=(S^2-Q)/2

            Now we know:

            c+d=S
            cd=(S^2-Q)/2

            Hence c and d are roots of:

            x^2-Sx+cd=0

            Using the Quadratic Formula:

            c=(S+sqrt(2Q-S^2))/2
            d=(S-sqrt(2Q-S^2))/2

            gg :)
        '''

        S = 2 * sum(set(nums)) - sum(nums)
        Q = 2 * sum(x * x for x in set(nums)) - sum(x * x for x in nums)

        root = isqrt(2 * Q - S * S)

        c = (S + root) // 2
        d = (S - root) // 2

        return [c, d]