import numpy as np
import math as m

def grid_difference(grid_1, grid_2):
    grid_d = []
    N = len(grid_1)
    for i in range(N):
        grid_d.append([])
        for j in range(N):
            if grid_1[i][j] == grid_2[i][j]:
                grid_d[i].append(-1)
            else:
                grid_d[i].append(1)
    return grid_d


def magnetization(grid):
    N_up = 0
    N_down = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] > 0:
                N_up += 1
            else:
                N_down += 1
    M = (N_up - N_down)/len(grid)**2

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
