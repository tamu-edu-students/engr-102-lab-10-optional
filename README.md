# ENGR 102 Lab Topic 10 (optional)

## Activities
This **optional** lab consists of four activities. Please submit the following files to Gradescope.

1. [Debugging Code](#debugging-code)
2. [Guessing Game](#guessing-game)
3. [Sum Squares](#sum-squares)
4. [No Three in a Line](#no-three-in-a-line)

## Debugging Code
Open the Excel file `thermo_properties.xlsx`. This document lists thermodynamic properties of liquid water at varying temperatures and at two different pressures. The properties listed are as follows:
- Specific volume `v` in units of m^3⁄kg
- Specific internal energy `u` in units of kJ/kg
- Specific enthalpy `h` in units of kJ/kg
- Specific entropy `s` in units of kJ/(kg∙K)

It is common to use linear interpolation for temperature values not listed. So, for properties at T=25 C, you need to interpolate between the property values listed for T=20 C and T=40 C. It is also common to interpolate between pressure values as well. When both temperature and pressure values are not listed, it is necessary to perform a double interpolation. Check out the [double interpolation example video posted here](https://mediasite.tamu.edu/Mediasite/Play/476b08709b2f4e30ac4fde6812b9707f1d) for an explanation of the math.

Open the file `buggy_code.py`. In this file, the temperature and property values for P=5 MPa and P=10 MPa have been hard-coded **as lists** for temperatures from T=0 C to T=260 C. The program takes as input a temperature and pressure from the user, finds the two values of temperature that bracket the user's value, then performs a double linear interpolation for all four properties. The results are formatted and printed to the screen using 7, 2, 2, and 4 decimal places for the specific volume, specific internal energy, specific enthalpy, and specific entropy, respectively.

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



## Sum Squares


## No Three in a Line


Revised Summer 2026 SNR
