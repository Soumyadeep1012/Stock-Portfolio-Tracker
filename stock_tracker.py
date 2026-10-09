# Stock Portfolio Tracker
# This program calculates total investment
# using manually defined stock prices.

from datetime import datetime
import csv
import os


# -----------------------------------------
# 1. Hardcoded stock prices
# -----------------------------------------

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400
}


# -----------------------------------------
# 2. Store portfolio information
# -----------------------------------------

portfolio = []
total_investment = 0


# -----------------------------------------
# 3. Get current date and time
# -----------------------------------------

entry_time = datetime.now()
formatted_time = entry_time.strftime("%d-%m-%Y %H:%M:%S")


# -----------------------------------------
# 4. Display available stocks
# -----------------------------------------

print("\n========== STOCK PORTFOLIO TRACKER ==========\n")

print("Available Stocks:")

for stock in stock_prices:
    print(stock, "- $", stock_prices[stock])


# -----------------------------------------
# 5. Ask how many stocks to enter
# -----------------------------------------

while True:

    try:
        number_of_stocks = int(
            input("\nHow many different stocks do you want to enter? ")
        )

        if number_of_stocks > 0:
            break

        print("Please enter a number greater than 0.")

    except ValueError:
        print("Invalid input. Please enter a whole number.")


# -----------------------------------------
# 6. Take stock information
# -----------------------------------------

for i in range(number_of_stocks):

    print("\n---------- Stock", i + 1, "----------")

    stock_name = input("Enter the stock name: ").upper()

    if stock_name not in stock_prices:
        print("Sorry, that stock is not available.")
        continue

    while True:

        try:
            quantity = int(input("Enter the quantity: "))

            if quantity > 0:
                break

            print("Quantity must be greater than 0.")

        except ValueError:
            print("Invalid quantity. Please enter a whole number.")

    price = stock_prices[stock_name]

    investment = price * quantity

    total_investment = total_investment + investment

    portfolio.append({
        "stock": stock_name,
        "price": price,
        "quantity": quantity,
        "investment": investment
    })

    print("Investment for", stock_name, ":", "$", investment)


# -----------------------------------------
# 7. Display portfolio summary
# -----------------------------------------

print("\n\n========== PORTFOLIO SUMMARY ==========\n")

if len(portfolio) == 0:

    print("No valid stocks were added to the portfolio.")

else:

    print("Entry Date & Time:", formatted_time)
    print()

    print(
        "{:<10} {:<10} {:<12} {:<15}".format(
            "Stock",
            "Price",
            "Quantity",
            "Investment"
        )
    )

    print("-" * 47)

    for item in portfolio:

        print(
            "{:<10} ${:<9} {:<12} ${:<15}".format(
                item["stock"],
                item["price"],
                item["quantity"],
                item["investment"]
            )
        )

    print("-" * 47)

    print(
        "{:<32} ${}".format(
            "TOTAL INVESTMENT:",
            total_investment
        )
    )


# -----------------------------------------
# 8. Ask whether to save the portfolio
# -----------------------------------------

if len(portfolio) > 0:

    while True:

        save_choice = input(
            "\nDo you want to save the portfolio?\n"
            "1. Save as TXT\n"
            "2. Save as CSV\n"
            "3. Do not save\n"
            "Enter your choice: "
        )

        if save_choice in ["1", "2", "3"]:
            break

        print("Invalid choice. Please enter 1, 2, or 3.")


    # -----------------------------------------
    # 9. Save as TXT without deleting history
    # -----------------------------------------

    if save_choice == "1":

        with open("portfolio.txt", "a") as file:

            file.write("\n")
            file.write("========================================\n")
            file.write("STOCK PORTFOLIO ENTRY\n")
            file.write("========================================\n")
            file.write("Entry Date & Time: " + formatted_time + "\n\n")

            for item in portfolio:

                file.write("Stock: " + item["stock"] + "\n")
                file.write(
                    "Price per share: $" +
                    str(item["price"]) + "\n"
                )
                file.write(
                    "Quantity: " +
                    str(item["quantity"]) + "\n"
                )
                file.write(
                    "Investment: $" +
                    str(item["investment"]) + "\n"
                )
                file.write("\n")

            file.write(
                "Total Portfolio Investment: $" +
                str(total_investment) +
                "\n"
            )

        print("\nNew portfolio entry added to portfolio.txt.")
        print("Previous entries were preserved.")


    # -----------------------------------------
    # 10. Save as CSV without deleting history
    # -----------------------------------------

    elif save_choice == "2":

        file_exists = os.path.exists("portfolio.csv")

        with open(
            "portfolio.csv",
            "a",
            newline=""
        ) as file:

            writer = csv.writer(file)

            if not file_exists:

                writer.writerow([
                    "Entry Date & Time",
                    "Stock",
                    "Price",
                    "Quantity",
                    "Investment"
                ])

            for item in portfolio:

                writer.writerow([
                    formatted_time,
                    item["stock"],
                    item["price"],
                    item["quantity"],
                    item["investment"]
                ])

            writer.writerow([
                formatted_time,
                "TOTAL",
                "",
                "",
                total_investment
            ])

        print("\nNew portfolio entry added to portfolio.csv.")
        print("Previous entries were preserved.")


    # -----------------------------------------
    # 11. Do not save
    # -----------------------------------------

    else:

        print("\nPortfolio was not saved.")

else:

    print("\nNo portfolio file was created.")