# Problem Statement

Managing daily expenses manually can be difficult and time-consuming. It can also become hard to remember where money was spent and how much was spent.

The aim of this project is to create a simple **Daily Expense Tracker using Python** that helps users record and manage their daily expenses. The program provides options to add, view, search and delete expenses.

It also calculates total and average expenses and provides daily and overall expense summaries.

## Use of Text Files

The project uses text files for storing data instead of a database.

* **`data.txt`** stores all expense records.
* **`budget.txt`** stores the monthly budget.

Each expense is stored in `data.txt` in this format:

```text
Date|Category|Amount|Description
```

Example:

```text
28-09-2026|Food|150.0|Lunch
28-09-2026|Travel|50.0|Bus
```

When the program starts, it reads the stored expenses from `data.txt`. When a new expense is added, it is saved to the file. If an expense is deleted, the file is updated with the remaining records.

The monthly budget entered by the user is saved in `budget.txt`.

Using text files makes the project simple and allows the data to remain available even after the program is closed.

## Main Objective

The main objective of this project is to make basic expense management easier while applying Python concepts such as:

* Functions
* File handling
* Lists
* Dictionaries
* Loops
* Conditional statements
* Exception handling
* `datetime`
