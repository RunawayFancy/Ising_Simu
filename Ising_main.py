import numpy as np
from tqdm import *
import pickle
import argparse
from metropolis import *
from tools import *
from copy import deepcopy

def get_grid(lst):
    if -1 in lst:
        index = np.where(np.array(lst)>-1)[0][0]
        grid = pickle.load(open(f"default_grid/default_grid_{lst[index]}.pkl", "rb"))
        # print(lst[index])
        # print(np.shape(grid))
    else:
        grid = np.random.choice([-1, 1], size=(lst[0], lst[1]))
    return grid

def get_param(args, grid):
    param = {"T":args.T, "trail": args.trail, "B":args.B, "J": args.J, "grid": grid, "scan_which": args.scan}
    param["scan"] = np.linspace(args.scan_rng[0], args.scan_rng[1], int(args.scan_rng[2]))
    del param[args.scan]

    return param

def ising_solve(args):
    grid0 = get_grid(args.grid)
    param = get_param(args, grid0)
    grid = deepcopy(grid0)
    avgM_lst = []; avgE_lst=[]; avgE2_lst=[];Cv_lst=[]
    not_scan = []
    if "B" in param: B = param["B"]; not_scan.append("B")
    if "J" in param: J = param["J"]; not_scan.append("J")
    if "T" in param: T = param["T"]; not_scan.append("T")
    trail = param["trail"]
    final_grid = []
    record_M = args.Mrecord

    if args.scan == "J":
        for J in tqdm(param["scan"]):
            result = solve_metropolis(T, grid, trail, B, J, record_M=record_M)
            avgM_lst.append(result[2]["avg_M"])
            avgE_lst.append(result[2]["avg_E"])
            avgE2_lst.append(result[2]["avg_E2"])
            Cv_lst.append(result[2]["Cv"])
            final_grid.append(result[0][-1])

    elif args.scan == "B":
        for B in tqdm(param["scan"]):
            result = solve_metropolis(T, grid, trail, B, J, record_M=record_M)
            avgM_lst.append(result[2]["avg_M"])
            avgE_lst.append(result[2]["avg_E"])
            avgE2_lst.append(result[2]["avg_E2"])
            Cv_lst.append(result[2]["Cv"])
            final_grid.append(result[0][-1])

    elif args.scan == "T":
        for T in tqdm(param["scan"]):
            result = solve_metropolis(T, grid, trail, B, J, record_M=record_M)
            avgM_lst.append(result[2]["avg_M"])
            avgE_lst.append(result[2]["avg_E"])
            avgE2_lst.append(result[2]["avg_E2"])
            Cv_lst.append(result[2]["Cv"])
            final_grid.append(result[0][-1])

    data = {
    "param": param,
    "avg_M": avgM_lst,
    "avg_E": avgE_lst,
    "avg_E2": avgE2_lst,
    "Cv": Cv_lst,
    "final_grid":final_grid
    }

    count, _ = pickle.load(open("counts.pkl", "rb"))

    filename = f"Ising_size_{np.shape(grid)[0]}x{np.shape(grid)[1]}_scan{args.scan}_{not_scan[0]}_{param[not_scan[0]]}_{not_scan[1]}_{param[not_scan[1]]}_{count}.pkl"

    pickle.dump(data, open(f"Data/"+filename, "wb"))

    pickle.dump([count+1, filename], open("counts.pkl", "wb"))
    print("Save as file "+filename)
    return 0

def parse_arguments():
    """
    # Passing example:
    # python .Ising_main.py --grid 20 20 --scan="J" --scan_rng 0 1 10 --T=1.25 --B=0.025 --trail=20000 --Mrecod=0
    """
    parser = argparse.ArgumentParser()
    # parser.add_argument('--note', type=str, default="fuck"
    #                     , help = '')
    parser.add_argument('--grid', nargs=2, type=int, default=[-1, 0], 
                        help='Read as a list: generate a 2D random grid with size of `grid`; if one of them is `-1`, then it use an default gird with index as the other one. e.g, grid = [-1, 0], then we use grid `default_grid_0.pkl`')
    parser.add_argument('--scan', type=str, default="J",
                        help='J, B, or T')
    parser.add_argument('--scan_rng', nargs=3, type=float, default=[0, 1, 1],
                        help='The scan range of J, B, or T. please refer to its input form')

    parser.add_argument('--J', type=float, default=None,
                        help='')
    parser.add_argument('--T', type=float, default=None,
                        help='')
    parser.add_argument('--B', type=float, default=None,
                        help='')
    parser.add_argument('--trail', type=int, default=1,
                        help='')
    parser.add_argument('--Mrecord', type=int, default=0,
                        help='1 for recoding <M>, takes for longer time.')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    # sys.exit(0)
    # get_grid(args.grid)
    ising_solve(args)
