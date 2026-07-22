class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)

        target = {}
        for word in words:
            target[word] = target.get(word, 0) + 1

        result = []

        for i in range(len(s) - total_len + 1):
            seen = {}

            for j in range(0, total_len, word_len):
                word = s[i + j:i + j + word_len]

                if word not in target:
                    break

                seen[word] = seen.get(word, 0) + 1

                if seen[word] > target[word]:
                    break
            else:
                result.append(i)

        return result
        