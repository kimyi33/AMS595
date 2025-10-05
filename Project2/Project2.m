% --- Main Experiment Setup ---
clear; clc; close all;

% 1. Define 1000 x-coordinates from -2 to 1
x_num = 1000;
x_vals = linspace(-2, 1, x_num);

% 2. Prepare a vector to store the y-coordinates of the boundary
y_boundary = zeros(size(x_vals));

% 3. Loop through each x-value
for i = 1:length(x_vals)
    x = x_vals(i); % Get the current x-value

    % 4. Define the indicator function for this specific x
    % It's negative inside the set and positive outside
    indicator_fn = @(y) (fractal(x + 1i * y) < 100) * 2 - 1;

    % 5. Use the bisection method to find the boundary (y-value)
    % A try-catch block handles cases where bisection might fail
    try
        y_boundary(i) = bisection(indicator_fn, 0, 2);
    catch
        y_boundary(i) = NaN; % Default to NaN if an error occurs
    end
end

% After the loop, the 'y_boundary' vector holds the fractal boundary.
% 5.You can visualize the result with a plot:
plot(x_vals, y_boundary, 'o', 'DisplayName', 'Mandelbrot Set Boundary');
title('Mandelbrot Set Boundary Points');
xlabel('Real(c)');
ylabel('Imag(c)');
axis equal;

% 6. Polynomial function fitting
% Create a logical index that is TRUE for all valid (not NaN) points
is_valid = ~isnan(y_boundary);

x_to_fit = x_vals(is_valid);
y_to_fit = y_boundary(is_valid);
p = polyfit(x_to_fit, y_to_fit, 15);
y_fit_curve = polyval(p,x_to_fit);

% 7.
l = poly_len(p,min(x_to_fit), max(x_to_fit));
hold on;
plot(x_to_fit, y_fit_curve, 'r-', 'LineWidth', 2, 'DisplayName', '15th Order Fit')
legend('Location', 'northwest');
hold off;

% Display the result
fprintf('Fineness of the measurement: %d, Length of the boundary: %.4f\n', x_num, l);