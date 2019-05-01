class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def maxDiff(list):
            n = len(list)
            maxRight = list[n -1]
            maxd = 0
            for i in range(n - 2, -1, -1):
                if list[i] > maxRight:
                    maxRight = list[i]
                else:
                    diff = maxRight - list[i]
                    if diff > maxd:
                        maxd = diff
            return maxd
        largest = 0
        total = 0
        for i in range(1, len(prices)):
            total = maxDiff(prices[:i]) + maxDiff(prices[i-1:])
            if total > largest:
                largest = total
        return largest
