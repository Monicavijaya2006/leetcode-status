class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        def power(x, n):
            if n == 0:
                return 1
            half = power(x, n // 2)
            if n % 2 == 0:
                return (half * half)%MOD
            else:
                return (half * half * x)%MOD
        r = ""
        for i in b:
            r += str(i)
        b = int(r)
        return power(a, b)