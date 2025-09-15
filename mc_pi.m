function est = mc_pi(k)
    % --- Initialization ---
    in_circle = 0;     % Number of points lie in a unit circle
    num_points = 0;    % Number of points generated
    sig_fig = k;       % Desired significant figure
    tolerance_counter = 0;   % tolerance counter for stability
    required_stable_iterations = 10^3;
    
    % Initialized estimates.
    prev_estimate = 0;
    last_estimate = 4;

    % Array to store (x, y) values
    xs = [];
    ys = [];

    
    while tolerance_counter < required_stable_iterations
        % Generate a single random point in the first quadrant.
        x = rand;
        y = rand;

        % Store x and y values
        xs(end+1) = x; % Append x value to xs array
        ys(end+1) = y; % Append y value to ys array
    
        % Increment total number of points.
        num_points = num_points + 1;
        
        % Check if the point is inside the unit circle.
        if x^2+y^2 <= 1
            in_circle = in_circle + 1;
        end
        
    
        % Calculate the new estimate for pi.
        last_estimate = 4*in_circle / num_points; % in_squre never be 0.
        
        % Stability check
        if abs(prev_estimate-last_estimate)< 10^(-sig_fig+1)
            tolerance_counter = tolerance_counter + 1;
        else
            tolerance_counter = 0;
        
        % Update the previous estimate with hte last estimate.
        prev_estimate = last_estimate;
    
        end
    end
    est = last_estimate;

    
    % Plot the points generated
    figure;
    inside = (xs.^2 + ys.^2 <=1);
    % Plot the points generated
    scatter(xs(inside), ys(inside), 'b.'); % Points inside the circle
    hold on;
    scatter(xs(~inside), ys(~inside), 'r.'); % Points outside the circle
    theta = linspace(0, pi/2, 200);
    plot(cos(theta), sin(theta), '-k')
    axis equal;
    title('Monte Carlo Simulation for \pi');
    xlabel('x-axis');
    ylabel('y-axis');
    text(0.85, 0.95, sprintf('\\pi \\approx %.4f', est), 'VerticalAlignment','top');

end