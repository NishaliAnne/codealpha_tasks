import csv

# Hardcoded stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 120,
    "MSFT": 300,
    "AMZN": 130
}

portfolio = {}  # To store user input: {stock_name: quantity}

print("📊 Welcome to Simple Stock Portfolio Tracker")

# Input loop
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in STOCK_PRICES:
        print("⚠️ Stock not in our price list. Try again.")
        continue
    try:
        qty = int(input(f"Enter quantity of {stock}: "))
        if qty <= 0:
            print("⚠️ Quantity must be positive.")
            continue
    except ValueError:
        print("⚠️ Enter a valid number.")
        continue

    if stock in portfolio:
        portfolio[stock] += qty
    else:
        portfolio[stock] = qty

# Calculate total investment
total_investment = 0
print("\n📈 Portfolio Summary")
print("-" * 40)
print("Stock | Quantity | Price | Value")
for stock, qty in portfolio.items():
    price = STOCK_PRICES[stock]
    value = qty * price
    total_investment += value
    print(f"{stock} | {qty} | {price} | {value}")

print("-" * 40)
print(f"💰 Total Investment: {total_investment}")

# Optional: save to CSV
save = input("Do you want to save the portfolio to CSV? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        for stock, qty in portfolio.items():
            writer.writerow([stock, qty, STOCK_PRICES[stock], qty * STOCK_PRICES[stock]])
        writer.writerow(["Total Investment", "", "", total_investment])
    print("✅ Portfolio saved to portfolio.csv")


