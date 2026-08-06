class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        final_profit = 0
        best_min = 100
        best_profit = 0
        

        for i in prices:
            if i < best_min:
                best_min = i
            elif i - best_min > best_profit:
                best_profit = i-best_min
        return best_profit