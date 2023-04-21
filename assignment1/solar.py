"""
leapint.py: program to integrate hamiltonian system using leapfrog.
"""
import numpy as np
import pandas as pd
import os

MAXPNT = 100


def main():

    # first, set up initial conditions
    n = 9  # set number of points
    tnow = 0.0  # set initial time

    # next, set integration parameters
    mstep = 256  # number of steps to take
    dt = 1.0 / 32.0  # timestep for integration

    # order: mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto
    distance = np.array([57900000.0, 108200000.0, 149600000.0, 227900000.0, 778600000.0, 1433500000.0, 2872500000.0, 4495100000.0, 5906380000.0]) #km
    distance = distance*10**3 # set it to 10^-12 meter scale
    x = np.zeros((n,3)) # 3-d position
    v = np.zeros((n,3))

    

    # set initial position and velocity 
    # assume only x-component velocity at start
    for i in range(n):
        x[i] = [np.sqrt((distance[i]**2)/2), np.sqrt((distance[i]**2)/2), 0]
        v[i] = [0.0,0.0,0.0]



    # intial sun position
    sun_pos = np.array([0.0, 0.0, 0.0])

    # Gravitational constant and Sun's mass
    G = 6.6743*10**-11
    M = 1.9891*10**30


    # delete old output if it exists
    if os.path.exists("solar.py.data"):
        os.remove("solar.py.data")    


    # save intial state
    save_state(n,x,tnow)

    # leapfrog integration
    for i in range(mstep):
        x, v = leapstep(x,v,n,dt,G,M, sun_pos)
        tnow = tnow + dt
        if i % 10 == 0:
            print(x[2])
        save_state(n, x, tnow)




def leapstep(x, v, n, dt, G, M, sun_pos):
    """LEAPSTEP: take one step using the leapfrog integrator, formulated
    as a mapping from t to t + dt.  WARNING: this integrator is not
    accurate unless the timestep dt is fixed from one call to another.
    Args:
        x (np.array): positions of all points
        v (np.array): velocities of all points
        n (int): number of planets
        dt (float): timestep for integration
        sun_pos (3-d np.array): position of the sun
    Returns:
        x:
        v:
    """
    
    v = v + 0.5*dt*accel(x,n,G,M,sun_pos)
    x = x + v*dt
    v = v + 0.5*dt*accel(x,n,G, M, sun_pos)

    return x,v


def accel(x: np.ndarray, n: int, G: float, M: float, sun_pos: np.ndarray):
    """ACCEL: compute accelerations for harmonic oscillator(s)
    Args:
        x a (array of shape (n, 3)): positions of planets
        n (int): number of planets
        G (float): gravitational constant
        M (float): mass of sun
        sun_pos a (array of shape (1,3)): position of the sun
    
    Returns:
        a (array of shape (N, 3)): accelerations of points
    """
    a = np.zeros((n,3))
    for i in range(n):
        r_vec = x[i] - sun_pos
        r_mag = np.sqrt((r_vec**2).sum())
        acc = -(G*M*r_vec/r_mag**3)
        #if i==2:
            #print(acc, r_vec)
        a[i] = acc
    return a

def save_state(n, x, tnow):
    """Save the current state to file.

    Args:
        n : size
        x (array of shape (N, 3)): positions of all points
        tnow (float): current time, in seconds
    """
    with open("solar.py.data", "a") as f:
        for i in range(n):  # loop over all points...
            f.write(format(tnow, '.5f') + " " + format(x[i][0], '12.6f') + " "+format(x[i][1], '12.6f') + " "+format(x[i][2], '12.6f')+ "\n")

main()