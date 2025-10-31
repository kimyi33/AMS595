import pandas as pd
import numpy as np
from sympy import symbols, diff, exp, sin, cos, factorial, lambdify
import matplotlib.pyplot as plt
import time

### Task 1 ###
def taylor_approx(func, start, end, degree, fixed_c):
    # Symbolic Taylor series to be made
    symbolic_poly = 0

    # Build Taylor series
    for i in range(degree+1):
        # Get i-th derivative
        diff_term = diff(func, x, i)
    
        # Get the value of derivative at c
        diff_val_at_c = diff_term.subs(x, fixed_c)
    
        # Add the term to the Taylor series
        term = diff_val_at_c * ((x - fixed_c)**i) / factorial(i)
        symbolic_poly += term
    # Convert symbolic polynomial to numpy polynomial
    numerical_poly = lambdify(x, symbolic_poly, 'numpy')

    # Generate x values and get approximation of y
    x_values = np.linspace(start, end, 100)
    y_approx = numerical_poly(x_values)
    
    return y_approx

### Task 2 ###
x = symbols('x')

# Given Inputs
func = x * sin(x) ** 2 + cos(x)
start = -10
end = 10
degree = 99
fixed_c = 0

# Approximate
y_approx = taylor_approx(func, start, end, degree, fixed_c)

# Plotting
x_values = np.linspace(start, end, 100)
y_actual = (lambda x: x * np.sin(x)**2 + np.cos(x))(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_approx, 'ro', label='Taylor Approximation', markersize=4)
plt.plot(x_values, y_actual, 'k-', label='Actual')
plt.xlabel('x')
plt.ylabel('$x \sin^2(x) + \cos(x)$')
plt.legend()
plt.savefig('taylor_figure.png')
plt.show()

### Task 3 ###
def analyze_taylor(initial_degree, final_degree, degree_step): 
    # We will make DataFrame with data
    data = []

    # For each degree m, we calculate the approximation time and total error
    for degree in range(initial_degree, final_degree + degree_step, degree_step):
        # Apprloximate y and time how long it takes
        start_time = time.time()
        y_approx = taylor_approx(func, start, end, degree, fixed_c)
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Calculate total error
        total_error = sum(abs(y_actual-y_approx))
        data.append([degree, elapsed_time, total_error])

    # Make DataFrame
    df = pd.DataFrame(data, columns=['degree', 'elapsed_time', 'total_error'])
    
    # Save the DataFrame to a CSV file as required
    df.to_csv('taylor_values.csv', index=False)

    return df
    
# Running the function
initial_degree = 50
final_degree = 100
degree_step = 10

analyze_taylor(initial_degree, final_degree, degree_step)
