class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != "[":
            return NestedInteger(int(s))

        stack = []
        num = ""

        for ch in s:
            if ch == "[":
                stack.append(NestedInteger())

            elif ch == ",":
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""

            elif ch == "]":
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""

                temp = stack.pop()
                result = temp

                if stack:
                    stack[-1].add(temp)

            else:
                num += ch

        return result