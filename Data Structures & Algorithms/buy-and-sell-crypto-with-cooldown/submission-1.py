class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = []
        # buy, sell, cooldown

        # dp
        # -1, 0 , 0
        # -3, 2, 0
        # -4, 1, 2
        # 2,

        for idx, p in enumerate(prices):
            if idx >= 1:
                buy = max(dp[idx-1][0], dp[idx-1][2] - p)
                sell = p + dp[idx-1][0]
                resting = max(dp[idx-1][1],dp[idx-1][2])
            else:
                buy = -p
                sell = 0
                resting = 0
            dp.append((buy,sell,resting))

        return max(dp[-1])
