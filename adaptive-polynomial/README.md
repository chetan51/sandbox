# Learning a single-variable polynomial, or the power of adaptive queries

An implementation of Jeremy Kun's article [Learning a single-variable polynomial, or the power of adaptive queries](http://jeremykun.com/2014/11/18/learning-a-single-variable-polynomial-or-the-power-of-adaptive-queries/).

## Usage

First, run `python polynomial.py` to generate a polynomial. Then run `guesser.py` to have it guess your generated polynomial using adaptive querying.

## Example

    » python polynomial.py
    What is the degree of the polynomial?
    > 5

    Using polynomial of form:
    p(x) = a0N^0 + a1N^1 + a2N^2 + a3N^3 + a4N^4

    Enter coefficients:

    a0 = 39
    a1 = 48
    a2 = 3
    a3 = 40
    a4 = 2

    Using polynomial:
    p(x) = 39x^0 + 48x^1 + 3x^2 + 40x^3 + 2x^4

    p(1) = 132
    p(132 + 1) = p(133) = 719966412

    » python guesser.py
    Choose a polynomial with nonnegative integer coefficients, p(x).
    I'll ask you two questions, and then guess p(x).

    What is p(1)?
    > 132
    What is p(132 + 1) = p(133)?
    > 719966412

    Your polynomial, p(x), is:
    p(x) = 39x^0 + 48x^1 + 3x^2 + 40x^3 + 2x^4
