class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        l1 = len(num1) - 1
        l2 = len(num2) - 1
        l = []
        x = 0
        d = '0123456789'
        m = 0
        for i in range(l1, -1, -1):
            cnt = x
            f = '0'*x
            c = 0
            for j in range(l2, -1, -1):
                a = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                a = c + a
                if a > 9:
                    b = a % 10
                    c = a // 10
                else:
                    c = 0
                    b = a
                f = d[b] + f
                cnt += 1
            if c > 0:
                f = d[c] + f
                cnt += 1
            # print(f)
            l.append(f)
            x += 1
            if cnt > m:
                m = cnt
        # print(m)
        f = ''
        c = 0
        # print('add')
        m1 = -1
        while (-1)*m1 <= m:
            a = 0
            for i in l:
                try:
                    a += (ord(i[m1]) - ord('0'))
                except IndexError:
                    a += 0
            # print(a)
            a = c + a
            if a > 9:
                b = a % 10
                c = a // 10
            else:
                c = 0
                b = a
            f = d[b] + f
            m1 -= 1
        if c > 0:
            f = d[c] + f
        return f
        