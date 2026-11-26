# Personal Finance & Inflation Budget Simulator

A small command-line Python program that projects your savings balance over 5 years, taking inflation on your fixed expenses and interest on your savings into account.

## Features

- Create your own profile: income streams, fixed expenses (with yearly inflation %), current savings and savings interest rate
- Load a built-in sample profile to try it quickly
- 5-year (60-month) projection with a yearly summary table
- Input validation so wrong entries do not crash the program

## How it works

Every month the balance is updated as:

```
balance = balance + (balance x annual_rate / 1200) + total_income - total_expenses
```

- Each fixed expense grows once a year: `amount x (1 + inflation/100) ** year`
- Interest is applied monthly (annual rate divided by 12)
- A table is printed at the end of every year, followed by the final balance

## Requirements

- Python 3.6 or newer (no external libraries)

## Run

```bash
python main.py
```

## Menu

| Option | Action |
|--------|--------|
| 1 | Create a new profile |
| 2 | Load the sample profile |
| 3 | Run the 5-year projection |
| 4 | Exit |

## Sample output (sample profile)

```
Year |Income/mo|Expense/mo|       Balance
1    |    60000|     25000|    645,901.90
2    |    60000|     26500|  1,103,354.29
3    |    60000|     28090|  1,571,784.31
4    |    60000|     29775|  2,050,747.60
5    |    60000|     31562|  2,539,699.31
Final balance after 5 years: Rs 2,539,699.31
```

## Project structure

```
.
├── main.py
├── README.md
└── .gitignore
```
