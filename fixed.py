def total_price(prices):
    total = 0
    for price in prices:
        total = total + price
    return total

print("Total:", total_price([10, 25, 7, 42]))
