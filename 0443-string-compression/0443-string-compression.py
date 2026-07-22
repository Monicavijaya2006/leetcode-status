class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = chars[0]
        cnt = 1
        i = 0

        for r in range(1, len(chars)):
            if prev != chars[r]:
                chars[i] = prev
                i += 1

                if cnt > 1:
                    for c in str(cnt):
                        chars[i] = c
                        i += 1

                prev = chars[r]
                cnt = 1
            else:
                cnt += 1

        chars[i] = prev
        i += 1

        if cnt > 1:
            for c in str(cnt):
                chars[i] = c
                i += 1

        return i