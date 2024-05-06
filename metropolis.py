import random
import numpy as np
import math as m
# from tools import magnetization
from tqdm import *
from copy import deepcopy


def magnetization(grid):
    """
    Use np array to speed up the calculation
    """
    grid = np.array(grid)
    N_up = np.sum(grid > 0)
    N_down = np.sum(grid <= 0)
    M = (N_up - N_down) / grid.size
    return M

# def magnetization(grid):
    # N_up = 0
    # N_down = 0
    # for i in range(len(grid)):
    #     for j in range(len(grid)):
    #         if grid[i][j] > 0:
    #             N_up += 1
    #         else:
    #             N_down += 1
    # M = (N_up - N_down)/len(grid)**2
    # return M
        
def f(delta_energy, T):
    """
    Probability density function based on Boltzmann distibution
    """
    return m.exp(- delta_energy/T)

def energy_k(grid,k,B,J):
    row, column = position_cal(k,grid)
    sum_spin = 0
    ## Only accepting adjacent neighbors, not diagonal neighbors
    N = len(grid)
    sum_spin += grid[row,(column+1)%N]   + grid[row,(column-1)%N]  +  grid[(row+1)%N,column]   +  grid[(row-1)%N,column]
    sum_spin *= 1/2  ## Avoids double counting
    E_k =  -J* sum_spin* grid[row][column] - B*grid[row][column]
    return E_k

def energy_total(grid,B,J):
    E_total = 0
    for i in range(len(grid)**2):
        E_i = energy_k(grid,i,B,J)
        E_total += E_i
    return E_total

# def spin_flip(grid,k):
#     N = len(grid)
#     grid_flip = []
#     row, column = position_cal(k,grid)
#     for i in range(N):
#         grid_flip.append([])
#         for j in range(N):
#             n = grid[i][j]
#             if [i,j] == [row, column]:
#                 n = -n
#             grid_flip[i].append(n)

#     return grid_flip

def spin_flip(grid,k):
    row, column = position_cal(k,grid)
    grid_flip = np.copy(grid)
    grid_flip[row][column] *= -1
    return grid_flip

def position_cal(k, grid):
    size = len(grid)
    row = int(np.floor(k/size))
    column = k - row*size
    return row,column

def solve_metropolis(T:float, grid, trails:int, B:float, J:float, record_M=0, change_temperature=False, T_change_amount=0):
    # Assume the gird is a N by N array with value either +1 or -1
    # Assume the Boltzmann constant k = 1
    accept = 0  
    record = 0
    N = len(grid)

    # Define the out put quantity
    magnetizationData = []
    del_energies = []
    mag = []
    correlation_function = []
    specific_heat = []
    oldGrids = []

    # print('This is working')

    for p in tqdm(range(trails),leave=None):
        ### Create a check to run 10 times during the process
        if p%(np.floor(trails/20))==0:
            currentMag = magnetization(grid)
            magnetizationData += [currentMag]
            oldGrids += [grid]
            # print('After',p,'trials, the current magnetization is: M =',currentMag)
        # Select via random vertexes
        k = random.randint(0,N**2-1)
        delta_E = -2* energy_k(grid,k,B,J) #- energy_k(grid,k,B)
        if(delta_E < 0 or f(delta_E, T) >= np.random.uniform(0,1)):
            grid = spin_flip(grid,k)
            accept += 1
        if p > trails//2:
            if record == 0:
                grid_ref = deepcopy(grid)
                record = 1
            else:
                del_energies.append(delta_E)
                if record_M==1:
                    mag.append(magnetization(grid))
    oldGrids.append(grid)

    # Calculate the average energy
    E_ref = energy_total(grid_ref, B, J)
    energies=[E_ref]
    for ii in range(len(del_energies)):
        energies.append(energies[ii] + del_energies[ii])
    avg_energy = np.mean(energies)
    if len(mag) >0:
        avg_magnetization = np.abs(np.mean(mag))
    else: 
        avg_magnetization = 0
    energy_sq = np.mean([e**2 for e in energies])
    specific_heat = (energy_sq - avg_energy**2) / (T**2)
        
    # print("Change temperature: {} \n".format(change_temperature))
    # print("Temperature changed amount: {} \n".format(T_change_amount))
    # print("Total numbers of attempts: {} \n".format(trails))
    # print("Numbers of successful flips: {} \n".format(accept))
    # print("Numbers of failed flips: {} \n".format(trails - accept))
    
    
    return [oldGrids, magnetizationData, {"avg_E": avg_energy, "avg_M": avg_magnetization,"avg_E2": energy_sq, "Cv": specific_heat}]

#     return grid, avg_energy, magnetization, specific_heat, correlation_function



