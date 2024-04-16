import random
import numpy as np
import math as m
import tools as tls


def f(delta_energy, T):
    """Probability density function based on Boltzmann distibution"""
    return m.exp(- delta_energy/T)


def energy_k(grid,k,external_field):
    row, column = position_cal(k,grid)
    sum_spin = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            sum_spin += grid[i][j]
    E_k = - (sum_spin - grid[row][column]) * grid[row][column] - external_field*grid[row][column]
    
    return E_k

def energy_total(grid,external_field):
    E_total = 0
    for i in range(len(grid)**2):
        E_i = energy_k(grid,i,external_field)
        E_total += E_i
        
    return E_total

def spin_flip(grid,k):
    N = len(grid)
    grid_flip = []
    row, column = position_cal(k,grid)
    for i in range(N):
        grid_flip.append([])
        for j in range(N):
            n = grid[i][j]
            if [i,j] == [row, column]:
                n = -n
            grid_flip[i].append(n)

    return grid_flip
    
def position_cal(k, grid):
    size = len(grid)
    row = int(np.floor(k/size))
    column = k - row*size
    
    return row,column

def solve_metropolis(T, grid, repeat_time, change_temperature, T_change_amount, external_field):
    # Assume the gird is a N by N array with value either +1 or -1
    # Assume the magnetic coupling constant J = 1
    # Assume the Boltzmann constant k = 1
    accept = 0  
    N = len(grid)

    # Define the out put quantity
    magnetization = []
    avg_energy = []
    correlation_function = []
    specific_heat = []

    # For an assigned spin, to calculate the correlation function
    r = 3
    i = 10
    j = i - r
    # Calculate the position information of sigma_i and sigma_j
    row_i,column_i = position_cal(i, grid)
    row_j,column_j = position_cal(j, grid)
    
    for p in range(repeat_time):
        E_assign = []
        M_assign = []
        spin_i_assign = []
        spin_j_assign = []

        if change_temperature == "False":
            pass
        else:
            T +=  T_change_amount
        for i in range(150):
            # Select via random vertexes
            k = random.randint(0,N**2-1)
                
            grid_flip = spin_flip(grid,k)
            delta_E = energy_k(grid_flip,k,external_field) - energy_k(grid,k,external_field)
            if(delta_E < 0 or f(delta_E, T) >= np.random.uniform(0,1)):
                grid = grid_flip
                accept += 1
            else:
                pass
            E_assign.append(energy_total(grid,external_field))
            M_assign.append(tls.magnetization(grid))
            spin_i_assign.append(grid[row_i][column_i])
            spin_j_assign.append(grid[row_j][column_j])
        correlation_function.append(tls.correlation_function(spin_i_assign,spin_j_assign, E_assign, T))
        avg_energy.append(tls.exp_value(E_assign,E_assign,T))
        magnetization.append(tls.exp_value(E_assign, M_assign, T))
        specific_heat.append(tls.specific_heat(E_assign, T))
        
    print("Change temperature: {} \n".format(change_temperature))
    print("Temperature changed amount: {} \n".format(T_change_amount))
    print("Total numbers of attempts: {} \n".format(repeat_time))
    print("Numbers of successful flips: {} \n".format(accept))
    print("Numbers of failed flips: {} \n".format(repeat_time - accept))
        
    return grid, avg_energy, magnetization, specific_heat, correlation_function