import numpy as np


def calculate_drag(rho, velocity, drag_coeff, ref_area):

    q = 0.5 * rho * np.abs(velocity) * velocity

    return - q * drag_coeff * ref_area
