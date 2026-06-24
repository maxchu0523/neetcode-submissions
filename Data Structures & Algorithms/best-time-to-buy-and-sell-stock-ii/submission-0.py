class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # action
        # buy
        # sell
        # on the same day
        # can only hold one share

        # hold
        # do nothing

        P = len(prices)
        memo = [ [0] * 4 for _ in range(P)]

        # action
        # buy, sell, do nothing

        # state
        # empty, holiding


        # state action
        # empty -> buy -> holding
        # holding -> sell -> empty
        # empty -> do nothing -> empty
        # holding -> do nothing -> holding
        
        memo[0][0] = -prices[0]
        memo[0][3] = -prices[0]
        
        for idx in range(1,P,1):
            memo[idx][0] = max(memo[idx-1][1], memo[idx-1][2]) - prices[idx]
            memo[idx][1] = max(memo[idx-1][0], memo[idx-1][3]) + prices[idx]
            memo[idx][2] = max(memo[idx-1][2], memo[idx-1][1])
            memo[idx][3] = max(memo[idx-1][0], memo[idx-1][3])
        return max(memo[-1])