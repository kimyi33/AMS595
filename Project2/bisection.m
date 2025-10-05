% Function m = bisection(fn_f, s, e)
% inputs:
% - fn_f: indicator function for a particular x
% - fn_f = @(y) (fractal(x+1i*y)>100)*2-1 % 1:divergence, -1:no-divergence
% - s: lower bound point, y
% - e: upper bound point, y
% output:
% - m: the boundary point of a fractal
function m = bisection(fn_f, s, e)
    % Ensure the signs at the start and end points are different.
    % This is a prerequisite for the bisection method to guarantee a solution.
    if sign(fn_f(s)) == sign(fn_f(e))
        error('The function must have different signs at the interval endpoints.');
    end

    while abs(e - s) > 1e-3 % Check for convergence
        m = (s + e) / 2; % Calculate the midpoint of the current interval.

        if sign(fn_f(m)) == sign(fn_f(s))
            % Sign changes in the upper half.
            s = m;
        else 
            % Sign changes in the lower half.
            e = m;
        end
    end
    m = (s+e) / 2;    % Return the final midpoint
end


 