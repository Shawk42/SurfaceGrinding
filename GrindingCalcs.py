import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random as rand


"""
The purpose of this program is to model the surface grinding operation for further analysis.

The model is defined as a flat bar with three zones...
Zone 1 - Millscale - While this zone is typically ignored it was causing a problem for the operator
Zone 2 - Roughing - Normal grinding
Zone 3 - Finishing - The finishing passes on the part
"""

"""Is scale a factor?"""
scale = input("Is scale a factor [yes or no]")


"""Model inputs"""
n = 100                                #"Mesh" size
thick_piece = .375
thick_tgt = .25

if scale == "yes":
    S_thick = np.linspace(0,.0039,num=n)     #Thickness of the millscale with a max thickness of .0039
    S_pd = np.linspace(.0015,.0005,num=n)     #Pass depth for scale
    print("Scale is factor")
else:
    S_thick = np.linspace(0,0, num=n)  # Thickness of the millscale with a max thickness of .0039
    S_pd = np.linspace(.0015, .0005, num=n)  # Pass depth for scale
    print("Scale is not a factor")

F_thick_nom = np.linspace(.001,.005,num=n)     #Thickness of finishing region
F_pd_nom = np.linspace(.001,.002,num=n)        #Pass depth for finishing

R_pd_nom = np.linspace(.001,.007,num=n)        #Pass depth for roughing

"""Random Sampling Loop"""
gamma = 1000                 #number of interations to run
gamma_count = 0
while gamma_count <= gamma:
    F_thick = np.random.permutation(F_thick_nom)
    F_pd = np.random.permutation(F_pd_nom)
    R_pd = np.random.permutation(R_pd_nom)


    thick = thick_piece-thick_tgt                       #Amount of material to be removed
    R_thick = thick-S_thick-F_thick    #Thickness of roughing region
    S_pass = S_thick/S_pd             #Number of passes for the scale region
    R_pass = R_thick/R_pd             #Number of passes for the roughing region
    F_pass = F_thick/F_pd             #Number of passes for the finishing region
    Pass_tot = S_pass+R_pass+F_pass   #Total number of passes required

    S_per = np.average((S_pass/Pass_tot)*100)
    R_per = np.average((R_pass/Pass_tot)*100)
    F_per = np.average((F_pass/Pass_tot)*100)

    gamma_count += 1

print("-"*50)
print("Percentage output")
print("-"*50)

print(int(S_per), "% in scale")
print(int(R_per), "% in rough")
print(int(F_per), "% in finish")

print("-"*50)
print("Time output [in minutes]")
print("-"*50)
t = 120
t_scale = int(t*(S_per/100))
t_rough = int(t*(R_per/100))
t_finish = int(t*(F_per/100))

print(t_scale,"minutes spent in scale")
print(t_rough,"minutes spent in roughing")
print(t_finish, "minutes spent in finishing")

sum = int(S_per+R_per+F_per)

if sum >= 99:
    print("Summation is greater than or equal to 99")
else:
    print("Summation is less 99")

"""If the process took an hour analysis"""


