import numpy as np
from scipy.integrate import odeint


N = 2500
R0 = 1.5
gamma = 1/7  #Give a value to gamma for SIR model (no isolation)
beta = (R0 * gamma) / N
print('Use R0 to calculate beta without any intervention: R_0 ',R0,'gamma ',gamma,'beta',beta)

y0 = [2495, 5, 0] #Set initial conditions for S, I, and R, in that order


t_range = np.arange(0.0, 200.0, 0.1) #Set the time range to be t=0 to t=15, with time steps of 0.1 when numerically solving

def model(y, t):
    S, I, R = y #Define y as consisting of S, I, and R, in that order
    dydt = [-beta * S * I, beta * S * I - gamma * I, gamma * I] #Provide the right-hand sides of the SIR model
    return dydt

sol = odeint(model, y0, t_range) #Give the name "sol" to the lists of numerical values in the solution, and give "odeint" the information needed to solve

