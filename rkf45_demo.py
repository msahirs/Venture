import numpy as np
from matplotlib import pyplot as plt
from Integrators import TimeIntegrator as integrate

def dydt(t,y):
    rho = 1.

    if  45 > t > 40:
        cd = 0.05 + ((t)/40) * 1.5 
    else:
        cd = 0.05 

    s = 0.1
    m= 1
    # print(y[1])
    if t<15:
        thrust = 8000 - t * 8000/20
    else:
        thrust = 0

    drag = 0.5 * rho * np.abs(y[1,0]) * y[1,0] * cd * s


    
    a = (thrust - drag)/m - 9.81
    
    return np.array([[y[1,0],a]]).T

def main():
    # ans = euler(np.array([5,2]),dydt,0,1000,0.001)
    ans = integrate.rkf45(np.array([[5,2]]).T, dydt, 0, 1000, 1, 1e-6)
    print(ans)
    plt.plot(ans[1],ans[2][0])

    plt.show()


if __name__ == '__main__':

    main()