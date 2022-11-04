import numpy as np


class TimeIntegrators:
    """
    Class of time-variant integrators
    
    
    """

    def __init__(self) -> None:
        pass
        
    def rkf45(y_initial, dydt, t_initial, t_end, stepSize, setAdaptive = True, adaptiveMethod= "simple", adaptiveParams = 1.2, errorTol = 1e-6, setLogging = True):

        rk_A = [0, 2/9, 1/3, 3/4, 1, 5/6]

        rk_B = [
                 [0, 0, 0, 0, 0],
                 [2/9, 0, 0, 0, 0],
                 [1/12, 1/4, 0, 0, 0],
                 [69/128, -243/128, 135/64, 0, 0],
                 [-17/12,  27/4, -27/5,  16/15, 0],
                 [65/432, -5/16,  13/16, 4/27,  5/144] ]

        rk_CH = [47/450, 0, 12/25, 32/225, 1/30, 6/25]

        rk_CT = [-1/150, 0, 3/100, -16/75, -1/20, 6/25]

        #--------------------------------------------------
        stepsize_copy = stepSize

        history = np.copy(y_initial)
        
        time_history = np.array([t_initial])

        while t_initial < t_end and y_initial[0,0] > 0:

            
            k1 = stepSize * dydt(t_initial + rk_A[0] * stepSize,y_initial)
            k2 = stepSize * dydt(t_initial + rk_A[1] * stepSize, y_initial + rk_B[1][0] * k1)
            k3 = stepSize * dydt(t_initial + rk_A[2] * stepSize, y_initial + rk_B[2][0] * k1 + rk_B[2][1] * k2)
            k4 = stepSize * dydt(t_initial + rk_A[3] * stepSize, y_initial + rk_B[3][0] * k1 + rk_B[3][1] * k2 + rk_B[3][2] * k3)
            k5 = stepSize * dydt(t_initial + rk_A[4] * stepSize, y_initial + rk_B[4][0] * k1 + rk_B[4][1] * k2 + rk_B[4][2] * k3 + rk_B[4][3] * k4)
            k6 = stepSize * dydt(t_initial + rk_A[5] * stepSize, y_initial + rk_B[5][0] * k1 + rk_B[5][1] * k2 + rk_B[5][2] * k3 + rk_B[5][3] * k4 + rk_B[5][4] * k5)

            if setAdaptive:  
                
                trunc_error = np.linalg.norm(rk_CT[0] * k1 + rk_CT[1] * k2 + rk_CT[2] * k3 + rk_CT[3] * k4 + rk_CT[4] * k5 + rk_CT[5] * k6)
                
                if trunc_error > errorTol and adaptiveMethod == "simple":

                    stepSize_adapted = stepSize / adaptiveParams
                    stepSize = stepSize_adapted
                    continue


                elif trunc_error > errorTol and adaptiveMethod == "error":

                    stepSize_adapted = adaptiveParams * stepSize * (errorTol/trunc_error)**(0.2)
                    stepSize = stepSize_adapted
                    continue


            y_initial = y_initial + rk_CH[0] * k1 + rk_CH[1] * k2 + rk_CH[2] * k3 + rk_CH[3] * k4 + rk_CH[4] * k5 + rk_CH[5] * k6

            t_initial += stepSize

            if setLogging:

                history = np.hstack((history,y_initial))

                time_history = np.hstack((time_history,t_initial))

            stepSize = stepsize_copy
        

        if setLogging:
            return y_initial, time_history, history

        return y_initial


    def euler(y_initial, dydt, t_initial, t_end, stepSize, setLogging = True):

        history = np.copy(y_initial)
        time_history = np.array([stepSize])
        
        while t_initial < t_end and y_initial[0] > 0:

            y_initial = y_initial + stepSize * dydt(t_initial,y_initial)

            t_initial += stepSize

            if setLogging:

                history = np.hstack((history,y_initial))

                time_history = np.hstack((time_history,stepSize))


        if setLogging:
            return y_initial, time_history, history

        return y_initial

