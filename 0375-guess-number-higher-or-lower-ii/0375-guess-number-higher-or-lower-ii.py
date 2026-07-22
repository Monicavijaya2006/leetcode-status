class Solution:
    def getMoneyAmount(self, n):

        @lru_cache(None)              # <-- we cache function results to avoid recomputing them
        def dp(l = 1, r = n)-> int:
            if r-l < 1: return 0      # <-- base case for the recursion; one number in [l,r]       
            ans = 1000                # <-- the answer for n = 200 is 952
            
            for choice in range((l+r)//2,r):
                ans = min(ans,choice+max(dp(l,choice-1),dp(choice+1,r)))

            return ans

        return dp()