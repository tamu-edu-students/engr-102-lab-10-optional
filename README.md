# ENGR 102 Lab Topic 10 (optional)

## Activities
This **optional** lab consists of four activities. Please submit the following files to Gradescope.

1. [Debugging Code](#debugging-code)
2. [Guessing Game](#guessing-game)
3. [Sum Squares](#sum-squares)
4. [No Three in a Line](#no-three-in-a-line)

## Debugging Code
Open the Excel file [`thermo_properties.xlsx`](thermo_properties.xlsx). This document lists thermodynamic properties of liquid water at varying temperatures and at two different pressures. The properties listed are as follows:
- Specific volume `v` in units of m^3⁄kg
- Specific internal energy `u` in units of kJ/kg
- Specific enthalpy `h` in units of kJ/kg
- Specific entropy `s` in units of kJ/(kg∙K)

It is common to use linear interpolation for temperature values not listed. So, for properties at T=25 C, you need to interpolate between the property values listed for T=20 C and T=40 C. It is also common to interpolate between pressure values as well. When both temperature and pressure values are not listed, it is necessary to perform a double interpolation. Check out the [double interpolation example video posted here](https://mediasite.tamu.edu/Mediasite/Play/476b08709b2f4e30ac4fde6812b9707f1d) for an explanation of the math.

Open the file [`buggy_code.py`](buggy_code.py). In this file, the temperature and property values for P=5 MPa and P=10 MPa have been hard-coded **as lists** for temperatures from T=0 C to T=260 C. The program takes as input a temperature and pressure from the user, finds the two values of temperature that bracket the user's value, then performs a double linear interpolation for all four properties. The results are formatted and printed to the screen using 7, 2, 2, and 4 decimal places for the specific volume, specific internal energy, specific enthalpy, and specific entropy, respectively.

At least, that's what this program is *supposed* to do. Instead, the file you are given has several bugs! Find and fix all of them. Rename the file `debugged_code.py` for submission. When debugging, remember DRIFT: discover, reproduce, isolate, fix, and test. It's a good idea to come up with several test cases to test your code **before** you start making changes.

Example output (using input `50` and `7.5`):
```
Enter a temperature between 0 and 260 deg C: 50
Enter a pressure between 5 and 10 MPa: 7.5
Properties at 50.0 deg C and 7.5 MPa are:
Specific volume (m^3/kg): 0.0010092
Specific internal energy (kJ/kg): 208.24
Specific enthalpy (kJ/kg): 215.81
Specific entropy (kJ/kgK): 0.6984
```


## Guessing Game
Write a python program named `guessing_game.py` to play a number guessing game. Have your program display a short message with instructions, then continually prompt the user to guess a number. With each wrong guess, let the user know if their guess is too high or too low. When the user correctly guesses the number, output the total number of valid guesses made. **Write your program using at least two (2) functions and a try-except statement.** For the purposes of autograding, make your secret number `12`, and use the example output below for the text.

Example output:
```
Guess the secret number! Hint: it's an integer between 1 and 100...
What is your guess? 50
Too high!
What is your guess? 7
Too low!
What is your guess? 0.5
Bad input! Try again: 12
You guessed it! It took you 3 guesses.
```


## Sum Squares
In Fall 2023 ChatGPT (GPT-3.5) was given the following prompt:

*Write a Python function that takes as an argument a positive integer and returns a list of four numbers that when squared add up to the positive integer of interest*

The response is provided in the program named [`sum_squares.py`](sum_squares.py). Unfortunately, this code does not work for many numbers, and for very large numbers the code is extremely slow. Modify the function named `list_nums` to produce correct output in a reasonable amount of computational time. Please comment out any `input()` statements before submitting. It's okay to have `print()` statements.

As an example, `list_nums(15)` should return `[1, 1, 2, 3]` because `1^2 + 1^2 + 2^2 + 3^2 = 15`.

**Bonus:** Some numbers have multiple correct solutions. Write a function named `count_sets` that takes as a parameter a positive integer `n` and returns the number (count) of unique sets of four numbers that when squared add up to `n`. Include the function named as specified in your file.

## No Three in a Line
In Fall 2024 ChatGPT (GPT-3.5) was given the following prompt:

*Write a Python function that takes an argument n and returns the largest set of points of integer coordinates in an n by n grid such that no three points are in a line*

The response is provided in the program named [`no_three_in_a_line.py`](no_three_in_a_line.py). Unfortunately, this code does not work. Modify the function named `no_three_in_line` to return a set of points that satisfy the requirements in a reasonable amount of computational time. Please comment out any `input()` statements before submitting. It's okay to have `print()` statements.

Here are examples to get you started (there are many correct answers):
- `no_three_in_line(3)` may return `[[0, 0], [1, 1], [1, 2], [2, 0]]`
- `no_three_in_line(4)` may return `[[0, 0], [0, 1], [1, 1], [1, 2], [2, 0], [3, 2]]`

For grid sizes up to `n=46`, the conjectured largest set of points is `2n`. This can be difficult to solve with code, so your submission only needs to find a minimum of `n` points. **Bonus:** Have your code find `1.8n` or more points.


Revised Summer 2026 SNR
