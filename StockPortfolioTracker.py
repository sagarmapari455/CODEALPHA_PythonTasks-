import csv

# Hardcoded stock prices as per internship requirement
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "TCS": 3400,
    "INFY": 1500
}

portfolio = []

def add_stock():
    ticker = input("Enter Stock Symbol (AAPL/TSLA/GOOGL/MSFT/TCS/INFY): ").upper()
    
    if ticker not in STOCK_PRICES:
        print("❌ Stock not found in predefined price list!")
        return

    qty = int(input("Enter Quantity: "))

    portfolio.append({
        "ticker": ticker,
        "qty": qty,
        "price": STOCK_PRICES[ticker]
    })

    print("✅ Stock added!")

def view_portfolio():
    if not portfolio:
        print("📭 Portfolio is empty.")
        return
    
    total = 0
    print("\n---------- YOUR PORTFOLIO ----------")
    for stock in portfolio:
        investment = stock["qty"] * stock["price"]
        total += investment
        print(f"{stock['ticker']}  | Qty: {stock['qty']} | Price: {stock['price']} | Value: {investment}")

    print("-------------------------------------")
    print(f"✅ Total Investment Value: {total}")
    print("-------------------------------------\n")

def save_to_csv():
    filename = "portfolio_result.csv"
    
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Investment Value"])
        
        total = 0
        for stock in portfolio:
            value = stock["qty"] * stock["price"]
            total += value
            writer.writerow([stock["ticker"], stock["qty"], stock["price"], value])
        
        writer.writerow(["TOTAL", "", "", total])

    print(f"✅ Portfolio saved to {filename}")

def main():
    while True:
        print("""
==============================
   STOCK PORTFOLIO TRACKER
==============================
1. Add Stock
2. View Portfolio
3. Save to CSV
4. Exit
""")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            save_to_csv()
        elif choice == "4":
            print("✅ Exiting program...")
            break
        else:
            print("❌ Invalid choice!")

main()