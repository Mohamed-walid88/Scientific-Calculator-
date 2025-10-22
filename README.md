# Python Command-Line Scientific Calculator

A powerful, modular scientific calculator written in Python. It parses infix expressions (standard mathematical notation) and evaluates them, supporting a wide range of mathematical functions from basic arithmetic to combinatorics and trigonometry.

The core logic works in two main steps:
1.  **Infix to Postfix Conversion:** The `InfixToPostfix.py` script takes a user's input string (e.g., `5 + sin(90)`) and converts it into postfix notation (e.g., `5 90 sin +`) using a modified shunting-yard algorithm.
2.  **Postfix Evaluation:** The `CalculatePostfix.py` script reads the postfix expression, using a stack to perform the calculations in the correct order and produce the final result.

---

## Features

This calculator supports a wide variety of operations and functions:

### Basic Operations
* **Addition:** `+`
* **Subtraction:** `-`
* **Multiplication:** `*`
* **Division:** `/`
* **Modulo:** `%`
* **Exponentiation:** `^`
* **Parentheses:** `()`
* **Unary Minus (Negative Numbers):** `-` (e.g., `-5 + 10`)

### Trigonometric Functions
* `sin(d)`: Sine (d in degrees)
* `cos(d)`: Cosine (d in degrees)
* `tan(d)`: Tangent (d in degrees)
* `csc(d)`: Cosecant (d in degrees)
* `sec(d)`: Secant (d in degrees)
* `cot(d)`: Cotangent (d in degrees)

### Logarithmic Functions
* `ln(x)`: Natural Logarithm (base $e$)
* `log(x)`: Common Logarithm (base 10)
* `logB(x)`: Logarithm with a custom base $B$ (e.g., `log2(8)`)

### Combinatorics & Factorials
* `nPr(n, r)`: Permutations ($P(n, r)$)
* `nCr(n, r)`: Combinations ($C(n, r)$)
* `x!`: Factorial of $x$
* `Onto(m, n)`: Calculates the number of onto (surjective) functions from a set of size $m$ to a set of size $n$.
* `S(m, n)`: Stirling numbers of the second kind.

### Other Functions
* `sqrt(x)`: Square root of $x$
* `ceil(x)`: Ceiling function (rounds $x$ up)
* `floor(x)`: Floor function (rounds $x$ down)

---

## How to Run

This project is run from the command line.

1.  Make sure you have Python installed on your system.
2.  Ensure all the `.py` files are in the same directory.
3.  Run the main calculator file:
    ```bash
    python FinalCalculator.py
    ```
4.  The program will wait for you to type in your mathematical expression.
5.  Type your expression and press **Enter**.
6.  The calculator will print the result.

---

## Usage Examples

Here are some examples of expressions you can input:

### Basic Arithmetic
> (5 + 3) * 2 - 10 / 5
> 14.0

### Exponents and Unary Minus
> -5^2 + 10
> -15.0
*(Note: Follows order of operations, so `5^2` is calculated first, then made negative.)*

### Trigonometry (in degrees)
> sin(90) + cos(0) 2.0

### Logarithms
> log(100) + ln(7.389056) + log2(8) 7.0

### Combinatorics
> nCr(5, 2) + nPr(4, 3) + 4! 58.0

### Other Functions
> sqrt(16) + ceil(2.1) + floor(5.9) 12.0

---

## Project File Structure

* `FinalCalculator.py`: The main entry point for the application. It takes user input and orchestrates the conversion and calculation process.
* `InfixToPostfix.py`: Contains the `Tokenizer` and logic for converting an infix expression string into a postfix expression string.
* `CalculatePostfix.py`: Contains the logic for parsing the postfix string and evaluating the final result using a stack.
* **Module Files** (`Sin.py`, `Cos.py`, `Log.py`, `Factorial.py`, `nCr.py`, `nPr.py`, etc.): Each file provides the implementation for a specific mathematical function, keeping the project modular and easy to maintain.
