% Function it = fractal(c)
% input: complex c
% output: 
% -it: how many iterations it takes for a point to diverge (|x|>2.0)
function it = fractal(c)
    z = 0;    % Start with z=0
    it = 0;    % output to find. # of iter.
    max_iter = 1000;
    while abs(z) <= 2.0 && it < max_iter
        z = z^2 + c;    % Equation (5.1)
        it = it + 1;    % Increment # of iter.
    end
end
