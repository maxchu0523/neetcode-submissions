class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        dp = [0] * (amount+1)
        for c in coins:
            for a in range(amount+1):
                if a == c:
                    dp[a] += 1
                if a - c > 0 and dp[a-c]:
                    dp[a] += dp[a-c]
        return dp[amount]
                