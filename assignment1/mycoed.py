"""
leapint.py: program to integrate hamiltonian system using leapfrog.
"""
import numpy as np

MAXPNT = 100


def main():
    x = np.zeros((MAXPNT))
    v = np.zeros((MAXPNT))

    # first, set up initial conditions
    n = 1  # set number of points
    x[0] = 1.0  # set initial position
    v[0] = 0.0  # set initial velocity
    out = np.zeros((256,4))
    out[0] = [0.0,0, 1.0, 0.0]

    # next, set integration parameters
    mstep = 256  # number of steps to take
    nout = 4  # steps between outputs
    dt = 1.0 / 32.0  # timestep for integration

    # now, loop performing integration
    for nstep in range(1,mstep):  # loop mstep times in all
        out[nstep] = leapstep(out[nstep-1][2], out[nstep-1][3], out[nstep-1][0], nstep, dt)  # take integration step

    for element in out:
        if element[1]%4 == 0:
            print(element)

def leapstep(x_start, v_start, t, index, dt):
    """LEAPSTEP: take one step using the leapfrog integrator, formulated
    as a mapping from t to t + dt.  WARNING: this integrator is not
    accurate unless the timestep dt is fixed from one call to another.
    Args:
        x (np.array): positions of all points
        v (np.array): velocities of all points
        n (int): number of points
        dt (float): timestep for integration
    """
    a = np.zeros((MAXPNT))
    v_half = 0.0
    x_next = 0.0
    v_next = 0.0
    acceleration = 0.0
    
    acceleration = accel(x_start)

    v_half = v_start + 0.5*acceleration*dt
    x_next = x_start + 0.5*v_half*dt 

    acceleration = accel(x_next)
    v_next = v_half + 0.5*acceleration*dt

    out = [t+dt, index, x_next, v_next]
    return out

def accel(x):
    """ACCEL: compute accelerations for harmonic oscillator(s)
    Args:
        a (np.array): accelerations of points
        x (np.array): positions of points
        n (int): number of points
    """
    acceleration = -x
    return acceleration  # use linear force law

if __name__ == "__main__":
    main()