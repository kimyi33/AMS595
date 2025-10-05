% Function l = poly_len(p, s, e)
% inputs:
% - p: fitted polynomial coefficients
% - s: left bound on x
% - e: right bound on x
% output:
% - l: the curve length of the polynomial

function l = poly_len(p, s, e)
    p_deriv = polyder(p);
    ds = @(x) sqrt(1 + polyval(p_deriv,x).^2);
    l = integral(ds, s, e);
end
