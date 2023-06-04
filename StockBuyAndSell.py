import math

def maximumProfit(prices):
    n = len(prices)
    minPrice = math.inf
    maxProfit=0
    for k in range(n):
        if prices[k]<minPrice:
            minPrice=prices[k]
        elif prices[k]-minPrice > maxProfit:
                maxProfit= prices[k]-minPrice
    return maxProfit
if __name__=="__main__":
    prices = [7,1,5,3,6,4]
    print(maximumProfit(prices))