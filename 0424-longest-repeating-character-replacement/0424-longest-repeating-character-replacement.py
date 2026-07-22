class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = [0] * 26
        max_cnt = 0
        ans = 0
        l = 0
        for i in range(len(s)):
            cnt[ord(s[i]) - ord("A")] += 1
            max_cnt = max(max_cnt, cnt[ord(s[i]) - ord("A")])
            if i - l + 1 - max_cnt > k:
                cnt[ord(s[l]) - ord("A")] -= 1
                l += 1
            ans = max(ans, i - l + 1)
        return ans