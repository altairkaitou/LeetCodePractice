class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
        for i in prices:
            min_price = min(min_price, i)
            max_profit = max(max_profit, i - min_price)
        if (max_profit == 0):
            return 0;
        return max_profit 
 