% --- Main Experiment Setup ---
clear; clc; close all;

% 1. Define the different values of x_num to test
x_num_vector = (1:30) * 100;

% 2. Prepare a vector to store the calculated length for each test
length_vector = zeros(size(x_num_vector));
fprintf('Starting the coastline paradox experiment...\n');

% 3. Loop through each value of x_num
for k = 1:length(x_num_vector)
    x_num = x_num_vector(k);
    fprintf('Calculating for x_num = %d...\n', x_num);

    % --- This is your existing calculation script, now inside a loop ---
    x_vals = linspace(-2, 1, x_num);
    y_boundary = zeros(size(x_vals));

    for i = 1:length(x_vals)
        x = x_vals(i);
        indicator_fn = @(y) (fractal(x + 1i * y) < 100) * 2 - 1;
        try
            y_boundary(i) = bisection(indicator_fn, 0, 2);
        catch
            y_boundary(i) = NaN;
        end
    end

    % Filter out NaN values first
    is_valid = ~isnan(y_boundary);
    x_to_fit = x_vals(is_valid);
    y_to_fit = y_boundary(is_valid);

    % Fitting and calculate the length
    p = polyfit(x_to_fit, y_to_fit, 15);
    y_fit_curve = polyval(p,x_to_fit);
    l = poly_len(p,min(x_to_fit), max(x_to_fit));
    length_vector(k) = l;    % Store
end
% --- 4. Plot the final results graph ---
figure;
plot(x_num_vector, length_vector, '-o', 'LineWidth', 2, 'MarkerFaceColor', 'b');
title('Coastline Paradox: Boundary Length vs. Measurement Fineness');
xlabel('Number of Sample Points');
ylabel('Approximate Length (l)');
grid on;

