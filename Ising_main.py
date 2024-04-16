import sys
import numpy as np
from tqdm import *
from time import *
from sympy import*
import copy
import pickle
import argparse





def ising_solve(args):
    
    return 0



def parse_arguments():
    """
    Passing example:
    python .\CZ_ST0_Ramsy.py --rt=128 --trail=8 --tau_list 500 600 30 --ep_list 10 10 1
    """
    parser = argparse.ArgumentParser()
    # parser.add_argument('--note', type=str, default="fuck"
    #                     , help = '')
    parser.add_argument('--N', type=int, default=2,
                        help='')
    parser.add_argument('--T0', type=int, default=0,
                        help='')
    parser.add_argument('--dBz', type=int, default=3.85e-3,
                        help='')
    parser.add_argument('--tau_list', nargs=3, type=int, default=[1, 1, 1],
                        help='')
    parser.add_argument('--ep_list', nargs=3, type=int, default=[1, 1, 1],
                        help='')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    # print(args.rt)
    # print(type(args.ep_list))
    # sys.exit(0)
    ising_solve(args)