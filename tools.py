import numpy as np
import math as m

def grid_difference(grid_1, grid_2):
    grid_1 = np.array(grid_1)
    grid_2 = np.array(grid_2)
    grid_d = np.where(grid_1 == grid_2, -1, 1)
    return grid_d


def magnetization(grid):
    """
    Use np array to speed up the calculation
    """
    grid = np.array(grid)
    N_up = np.sum(grid > 0)
    N_down = np.sum(grid <= 0)
    M = (N_up - N_down) / grid.size
    return M
        

def exp_value(E_assign, target_A, T):
    partition_function = 0
    numerator = 0
    for i in range(len(E_assign)):
        partition_function +=  np.exp(- E_assign[i]/T)
        numerator += np.exp(- E_assign[i]/T) * target_A[i]
    exp_val = numerator/partition_function

    return exp_val

def specific_heat(E_assign, T):
    E_2 = []
    for i in E_assign:
        E_2.append(i**2)
    c_v = (exp_value(E_assign, E_2, T) - (exp_value(E_assign, E_2, T))**2)/T**2

    return c_v

def correlation_function(spin_i_assign,spin_j_assign, E_assign, T):
    sigma_ij = []
    for k in range(len(spin_i_assign)):
        sigma_ij.append(spin_i_assign[k]*spin_j_assign[k])
    G_r = exp_value(E_assign,sigma_ij,T) - (exp_value(E_assign, spin_i_assign, T))**2

    return G_r
