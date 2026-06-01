# python--project-learn
A collection of simple Python projects built while learning programming fundamentals.

This repository contains my beginner Python mini projects. I built these to practice Python fundamentals y

## Projects

### 1. Smart Movie Tracker
A Python program that:
- Asks the user to enter 3 favorite movies
- Stores them in a list
- Asks for 1 recently watched movie
- Adds the new movie using `append()`
- Sorts the list alphabetically using `sort()`
- Prints the updated sorted list

**Concepts used:**
- `input()`
- Lists
- `append()`
- `sort()`
- Printing output

**How to run:**
```bash
python movie_tracker.py
```

### 2. Supermarket Bill & Discount Calculator
A Python program that:
- Takes prices of 3 grocery items
- Converts the inputs into `float`
- Stores the prices in a list
- Calculates the total bill
- Applies a discount using `if`, `elif`, and `else`
- Prints the original total, discount, and final amount

**Discount rules:**
- 10% discount for totals greater than or equal to 100
- 5% discount for totals between 50 and 99.99
- No discount for totals less than 50

**Concepts used:**
- `input()`
- `float()`
- Lists
- Arithmetic operators
- `if`, `elif`, `else`

**How to run:**
```bash
python bill_discount_calculator.py
```

### 3. Security Bot (Password Validator)
A Python program that:
- Takes a username and password from the user
- Checks whether the password is secure enough
- Shows a specific error if a rule fails
- Prints success if all rules pass

**Security rules:**
- Password must be at least 8 characters long
- Password must contain the `@` symbol
- Password must not be the same as the username

**Concepts used:**
- `input()`
- `len()`
- `in` keyword or `.count()`
- String comparison
- `if`, `elif`, `else`

**How to run:**
```bash
python password_validator.py
```

## What I learned
- How to take user input in Python
- How to store and update values in lists
- How to sort list data
- How to convert strings into numbers using `float()`
- How to use arithmetic in real programs
- How to apply conditions using `if`, `elif`, and `else`
- How to validate strings using `len()` and `in`
