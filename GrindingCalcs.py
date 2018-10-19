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

F_thick = np.linspace(.001,.005,num=n)     #Thickness of finishing region
F_pd = np.linspace(.001,.002,num=n)        #Pass depth for finishing

R_pd = np.linspace(.001,.005,num=n)        #Pass depth for finishing

"""Intermediate Calculations"""
thick = thick_piece-thick_tgt                       #Amount of material to be removed
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
ThickValid = "true"

"""Percentage Printing"""

S_pass_a = np.amax(S_pass)
R_pass_a = np.amax(R_pass)
F_pass_a = np.amax(F_pass)
Pass_tot_a = np.amax(Pass_tot)

S_per = (S_pass_a/Pass_tot_a)*100
R_per = (R_pass_a/Pass_tot_a)*100
F_per = (F_pass_a/Pass_tot_a)*100

print("-"*50)
print("Max percentages in simulation")
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

"""Validation"""
print("-"*50)
print("Data Checks")
print("-"*50)

if thick_tgt <= thick_piece:                                      #validating correct target vs initial
    print("VALID - Target thickness is less than total thickness")
else:
    print("INVALID - Target thickness is greater than total thickness")

if ThickValid == "true":                                        #moving routine check to validation section
    print("VALID - Every data point in valid")
else:
    print("INVALID - See first printed line")

if thick >= 0:                                             #is thickness to be removed positive
    print("VALID - Thickness to be removed in positive")
else:
    print("INVALID - Thickness to be removed is negative")

"""Percentage plotting"""

Scale_per_all = (S_pass/Pass_tot)*100
Rough_per_all = (R_pass/Pass_tot)*100
Finish_per_all = (F_pass/Pass_tot)*100


"""Plotting"""   #removed plotting due to focus
"""
#zero scale assumption
a = plt.plot(F_pass,R_pass)
plt.xlabel("Finishing Passes")
plt.ylabel("Roughing Passes")
plt.show(a)
"""

#3d plot - scale
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(S_pass,F_pass,R_pass, marker='*')
ax.set_xlabel("Scale Passes")
ax.set_zlabel("Roughing Passes")
ax.set_ylabel("Finishing Passes")
plt.show()

#3d plot - percentages
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(Scale_per_all,Finish_per_all,Rough_per_all, marker='*')
ax.set_xlabel("Scale %")
ax.set_zlabel("Roughing %")
ax.set_ylabel("Finishing %")
plt.show()
