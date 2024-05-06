index =2 : 500x500 preset

### Experiment 1

* Scan J

`python .\Ising_main.py --grid -1 2 --scan="J" --scan_rng 0 1 20 --T=1.25 --B=0.025 --trail=25000000 --Mrecord=1`

### Experiment 2

* Scan B

`python .\Ising_main.py --grid -1 2 --scan="B" --scan_rng 0 0.25 20 --T=1.25 --J=1 --trail=25000000 --Mrecord=1`

### Experiment 3

* Scan T

`python .\Ising_main.py --grid -1 2 --scan="T" --scan_rng 1e-8 5 20 --B=0.01 --J=1 --trail=25000000 --Mrecord=1`

##

1. <M> vs T, with three or four different J curve
2. The same for specific heat
3. Fit the log-log plot of the <M> transition part to get critical exponent alpha
4. Record spin diagram (Mag, thermal, transient)
5. flip-float picture Haha