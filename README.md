# Stock Portfolio Tracker 📈

## About the Project

I built this Stock Portfolio Tracker using Python. It is a simple program that helps me calculate how much money I have invested in different stocks.

The program has a list of four stocks with prices that I have set in the code. I can choose which stocks I want to add, enter the quantity, and see how much I have invested in each stock. At the end, the program shows a summary of my portfolio and the total investment.

I can also save my portfolio details in a TXT or CSV file. The program adds new entries without removing the older saved entries.

I made this project to practise Python and learn how to work with user input, lists, dictionaries, loops, functions from built-in modules, and files.

## Features

* Shows a list of available stocks and their prices.
* Lets me choose how many different stocks I want to enter.
* Takes the stock name and quantity from the user.
* Checks whether the stock is on the available list.
* Checks that the quantity is a valid whole number greater than zero.
* Calculates the investment for each stock.
* Shows the date and time when the program started recording the entry.
* Displays each stock's price, quantity, and investment in a table.
* Calculates and displays the total investment.
* Lets me save the portfolio as a TXT or CSV file.
* Keeps older saved entries when adding new ones.
* Allows me to finish without saving the portfolio.

## Stocks Available

The program currently uses these four stocks with fixed prices:

| Stock | Price per share |
| ----- | --------------: |
| AAPL  |            $180 |
| TSLA  |            $250 |
| GOOGL |            $150 |
| MSFT  |            $400 |

These prices are set manually in the code. The program does not get live stock prices from the internet.

## Requirements

To run this project, I need:

* Python 3 installed on my computer.
* A terminal or command prompt.

I do not need to install any extra Python packages. The program uses Python's built-in `datetime`, `csv`, and `os` modules.

## How to Run the Project

**Step 1:** Download or clone this repository.

```bash
git clone https://github.com/Soumyadeep1012/Stock-Portfolio-Tracker.git
```

**Step 2:** Open the project folder.

```bash
cd Stock-Portfolio-Tracker
```

**Step 3:** Run the Python file.

```bash
python stock_tracker.py
```

If `python` does not work on my computer, I can try:

```bash
py stock_tracker.py
```

## How to Use the Program

1. Run the program to see the available stocks and their prices.
2. Enter how many different stocks I want to add.
3. Enter a stock name, such as `AAPL` or `MSFT`.
4. Enter the quantity I want to include in the portfolio.
5. Repeat the process for the remaining stock entries.
6. Check the portfolio summary and total investment.
7. Choose whether to save the portfolio as a TXT file, a CSV file, or not save it.
8. Follow the message shown by the program to finish.

The program asks me to enter the information again if I enter an invalid number or quantity. If I enter a stock that is not on the available list, it skips that entry.

## How the Investment Is Calculated

The program uses a simple formula:

**Investment = Price per share × Quantity**

For example, if I select AAPL at $180 per share and enter a quantity of 5:

* Price per share: $180
* Quantity: 5
* Total investment: $900

The program uses the same calculation for every valid stock entry and adds the results to get the total investment.

## Saving Portfolio Details

I can choose between two file formats.

### 1. TXT File

The `portfolio.txt` file stores the portfolio details as readable text. It includes the date and time, stock names, prices, quantities, individual investments, and the total investment.

### 2. CSV File

The `portfolio.csv` file stores the data in rows and columns. I can open it in tools such as Microsoft Excel or Google Sheets to view the saved entries.

Both options add new portfolio entries while keeping the older saved data.

## What I Learned

While building this project, I practised:

* Taking input from the user and checking it.
* Using dictionaries to store stock prices.
* Using lists to store portfolio details.
* Using `for` and `while` loops.
* Using `if-else` conditions to handle different cases.
* Using `try-except` to handle invalid number input.
* Using `datetime` to get the current date and time.
* Using the `csv` module to save data in CSV format.
* Reading file and folder information with the `os` module.
* Adding new data to a file without removing older entries.
* Formatting output to make the portfolio summary easier to read.

## Future Improvements

I may improve this project later by adding live stock prices, more stocks, the option to remove or update entries, and a way to compare my portfolio over time.

## Author

**Soumyadeep Das**

GitHub: [Soumyadeep1012](https://github.com/Soumyadeep1012)

---

Thanks for checking out my project!
