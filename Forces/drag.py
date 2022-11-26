import numpy as np


def calculate_drag(rho, velocity, drag_coeff, ref_area):

    q = 0.5 * rho * np.abs(velocity) * velocity

    return - q * drag_coeff * ref_area


def calculate_drag_test(rho, velocity, drag_coeff, ref_area):
    ans = calculate_drag(rho, velocity, drag_coeff, ref_area)

    if np.sum(np.where(ans*velocity<0,1,0)) == 3:
        print("True")

    else:
        raise ArithmeticError("Drag vector not oppposite to velocity vector")



