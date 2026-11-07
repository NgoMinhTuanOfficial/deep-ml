import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    grad_arr = np.array(gradient)
    magnitude = np.sqrt(np.sum(grad_arr**2))

    if magnitude == 0:
        direction = np.zeros_like(grad_arr)
        descent_direction = np.zeros_like(grad_arr)
    else:
        direction = grad_arr / magnitude
        descent_direction = -direction
        
    return {
        'magnitude': float(magnitude),
        'direction': direction.tolist(),
        'descent_direction': descent_direction.tolist()
    }