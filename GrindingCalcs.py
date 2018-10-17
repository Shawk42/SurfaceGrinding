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
n = 1000                                  #"Mesh" size
thick = .125                             #Thickness of workpiece

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

"""Thickness validation"""
count = 0
thick_check = S_thick+F_thick+R_thick
while count != n:
    a = thick_check.item(count)
    if a == thick:
        count += 1
    else:
        dev = thick - a
        if dev <= .5:
            count += 1
        else:
            print(a,dev, "Deviation out of bounds")
print("Model is valid")



"""Percentage Printing"""

S_pass_a = np.amax(S_pass)
R_pass_a = np.amax(R_pass)
F_pass_a = np.amax(F_pass)
Pass_tot_a = np.amax(Pass_tot)

S_per = (S_pass_a/Pass_tot_a)*100
R_per = (R_pass_a/Pass_tot_a)*100
F_per = (F_pass_a/Pass_tot_a)*100

print("-"*50)
print("Percentages - Over entire spectrum")
print("-"*50)
print(S_per, "Scale passes percentage")
print(R_per, "Roughing passes percentage")
print(F_per, "Finishing passes percentage")

print("-"*50)
print("Max passes")
print("-"*50)
print(S_pass_a, "Max scale passes")
print(R_pass_a, "Max roughing passes")
print(F_pass_a, "Max finishing passes")
print(Pass_tot_a, "Max Passes")



"""Plotting"""   #removed plotting due to focus

#zero scale assumption
a = plt.plot(F_pass,R_pass)
plt.xlabel("Finishing Passes")
plt.ylabel("Roughing Passes")
plt.show(a)

#3d plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(S_pass,F_pass,R_pass, marker='*')
ax.set_xlabel("Scale Passes")
ax.set_zlabel("Roughing Passes")
ax.set_ylabel("Finishing Passes")
plt.show()

