class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        # 3D Memoization table: [idx][prev_index][sign]
        # signs: 0 = start, 1 = positive difference, 2 = negative difference
        memo = [[[-1 for _ in range(3)] for _ in range(n + 1)] for _ in range(n + 1)]

        def solve(idx, prev, prev_sign):
            # Base case: end of array
            if idx == n:
                return 0
            
            # Use prev + 1 to handle the initial -1 index safely
            if memo[idx][prev + 1][prev_sign] != -1:
                return memo[idx][prev + 1][prev_sign]

            take = 0
            # Option 1: Take the current number
            if prev == -1:
                # First element in subsequence
                take = 1 + solve(idx + 1, idx, 0)
            else:
                diff = nums[idx] - nums[prev]
                # If difference is negative and previous wiggle wasn't negative
                if diff < 0 and prev_sign != 2:
                    take = 1 + solve(idx + 1, idx, 2)
                # If difference is positive and previous wiggle wasn't positive
                elif diff > 0 and prev_sign != 1:
                    take = 1 + solve(idx + 1, idx, 1)

            # Option 2: Skip the current number
            skip = solve(idx + 1, prev, prev_sign)

            # Store the max result in memo
            ans = max(take, skip)
            memo[idx][prev + 1][prev_sign] = ans

            return ans

        # Start recursion from index 0, with no previous element and no sign
        return solve(0, -1, 0)