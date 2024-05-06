# For what

This project is served as the Final project of course PHY 403, Department of Physics and Astronomy, University of Rochester.

## Requirement

```
numpy==1.26.4
tqdm==4.66.1
ipywidgets
tkinter
IPython
```

## Method

we use Metropolis algorithm to find the ground state of a 2D Ising system.

## Usage

We use `argparse` to pass argument and execute the `Ising_main.py` simulation file in terminal.

### How to run simulation

Terminal under the directory of `\Ising_simu`.

> * **For windows power shell**
> An Example
> ```
> python .\Ising_main.py --grid 20 20 --scan="J" --scan_rng 0 1 10 --T=1.25 --B=0.025 --trail=20000 --Mrecod=0
> ```

### Argument 

> * `--gird`
>
> `nargs=2, type=int, default=[-1, 0]`
> Read as a list: generate a 2D random grid with size of `grid`; if one of them is `-1`, then it use an default gird with index as the other one. e.g, grid = [-1, 0], then we use grid `default_grid_0.pkl`

> * `--scan`
> 
> `type=str, default="J"`
> Which parameter want to scan: J, B, or T

> * `--scan_rng`
>
> `nargs=3, type=float, default=[0, 1, 1]`
> The scan range of J, B, or T. please refer to its input form

> * `--J`
> 
> `type=float, default=None`

> * `--T`
> 
> `type=float, default=None`

> * `--B`
> 
> `type=float, default=None` 

> * `--trail`
> 
> `type=int, default=1`
> Number of trails on each metropolis query, i.e., how many times to pick up a spin and exam whether flip it or not.

> * `--Mrecord`
>
> `type=int, default=0`
> `1` for recoding `<M>`, which will take a longer time.


### Make a plot

#### Data store

After download the code, create a folder named with `Data`, e.g., `Ising_simu\Data`.

All the plot code are in `Ising_simu\Simu_notebook\plot_sim.ipynb`.

#### Using `ipywidgets` to load data

```
import ipywidgets as widgets
from IPython.display import display
from tkinter import Tk, filedialog
import os

def select_files(b):
    root = Tk()
    root.withdraw()
    root.call('wm', 'attributes', '.', '-topmost', True)
    # Enable multiple file selection and set the initial directory
    filepaths = filedialog.askopenfilenames(initialdir="../Data/")
    root.destroy()
    # Extract filenames from the full paths and store them in a list
    filenames = [os.path.basename(filepath) for filepath in filepaths]
    print("Selected files:", filenames)
    b.filenames = filenames  # Store filenames in the button for further use if needed

fileselect = widgets.Button(description="Select Files")
fileselect.on_click(select_files)
```

Then, create a new python code section in `plot_sim.ipynb` and run code

```
display(fileselect)
```

Then, click the choose file.