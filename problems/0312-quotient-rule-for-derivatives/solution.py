import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    g_der_coe = np.polyder(g_coeffs)
    h_der_coe = np.polyder(h_coeffs)

    g_x = np.polyval(g_coeffs, x)
    h_x = np.polyval(h_coeffs, x)
    g_der_x = np.polyval(g_der_coe, x)
    h_der_x = np.polyval(h_der_coe, x)

    return (g_der_x*h_x - g_x*h_der_x)/(h_x**2)
    pass