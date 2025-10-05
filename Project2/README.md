# AMS 595 - Project 2: How Long Is the Coast of Britain?
This repository contains my MATLAB solutions for Project 2. The project builds bisection method to approximate the length of the boundary of the Mendelbrot fractal. This project has following steps:
* write a function computing the fractal
* use the bisection algorithm to approximate the boundary of the fractal
* use polynomial function approximation to find boundary as a function
* integrate the boundary curve to find its length

## Files
- `Project2_main.m` : This script calculates the length of the boundary of the Mendelbrot fractal.
    - Parameter: we need to set x_num and x_vals, to set the number of sample points of x
- `fractal.m`: This function takes complex c and returns the number of iterations till divergence
- `bisection.m`: This function finds the point at
which an indicator function switches sign.
- `poly_len`: This function computes the curve length of a polynomial.

## Usage
1. Ensure all `.m` files are in the same directory or added to the MATLAB path.
2. Open MATLAB and run the `Project2_main.m` script.