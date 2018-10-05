import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

"""
The purpose of this program is to model the surface grinding operation for further analysis.

The model is defined as a flat bar with three zones...
Zone 1 - Millscale - While this zone is typically ignored it was causing a problem for the operator
Zone 2 - Roughing - Normal grinding
Zone 3 - Finishing - The finishing passes on the part
"""

"""Model inputs"""
n = 500                                  #"Mesh" size
thick = .25                               #Thickness of workpiece

S_thick = np.linspace(0,.0039,num=n)     #Thickness of the millscale with a max thickness of .0039
S_pd = np.linspace(.0015,.0005,num=n)     #Pass depth for scale

F_thick = np.linspace(.001,.005,num=n)     #Thickness of finishing region
F_pd = np.linspace(.001,.002,num=n)        #Pass depth for finishing

R_pd = np.linspace(.001,.005,num=n)        #Pass depth for finishing

"""Intermediate Calculations"""
R_thick = thick-S_thick-F_thick    #Thickness of roughing region

"""Pass Number Cacluations"""
S_pass = S_thick/S_pd             #Number of passes for the scale region
R_pass = R_thick/R_pd             #Number of passes for the roughing region
F_pass = F_thick/F_pd             #Number of passes for the finishing region

Pass_tot = S_pass+R_pass+F_pass   #Total number of passes required


"""Plotting"""
plt.plot(R_pd,Pass_tot)
plt.xlabel("Roughing Pass Depth")
plt.ylabel("Number of Passes")
plt.title("Roughing Pass Depth vs. # of passes")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(S_pass,F_pass,R_pass, marker='*')
ax.set_xlabel("Scale Passes")
ax.set_zlabel("Roughing Passes")
ax.set_ylabel("Finishing Passes")
plt.show()




