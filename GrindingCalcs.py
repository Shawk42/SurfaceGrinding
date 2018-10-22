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

R_pd_nom = np.linspace(.001,.005,num=n)        #Pass depth for finishing

"""Random Sampling Loop"""
gamma = 100                 #number of interations to run
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
    S_pass_a = np.median(S_pass)
    R_pass_a = np.median(R_pass)
    F_pass_a = np.median(F_pass)
    Pass_tot_a = np.median(Pass_tot)
    S_per = (S_pass_a/Pass_tot_a)*100
    R_per = (R_pass_a/Pass_tot_a)*100
    F_per = (F_pass_a/Pass_tot_a)*100


    S_per_all = np.empty(gamma+1)
    S_per_all[gamma_count] = S_per

    F_per_all = np.empty(gamma+1)
    F_per_all[gamma_count] = F_per

    R_per_all = np.empty(gamma+1)
    R_per_all[gamma_count] = R_per
    gamma_count += 1


Mean_S = np.mean(S_per_all)
Mean_F = np.mean(F_per_all)
Mean_R = np.mean(R_per_all)

print(Mean_S,"Scale")
print(Mean_F,"Finish")
print(Mean_R,"Rough")






"""Plotting"""   #removed plotting due to focus
"""
#zero scale assumption
a = plt.plot(F_pass,R_pass)
plt.xlabel("Finishing Passes")
plt.ylabel("Roughing Passes")
plt.show(a)
"""
"""
#3d plot - scale
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(S_pass,F_pass,R_pass, marker='*')
ax.set_xlabel("Scale Passes")
ax.set_zlabel("Roughing Passes")
ax.set_ylabel("Finishing Passes")
plt.show()
"""
"""
#3d plot - percentages
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(Scale_per_all,Finish_per_all,Rough_per_all, marker='*')
ax.set_xlabel("Scale %")
ax.set_zlabel("Roughing %")
ax.set_ylabel("Finishing %")
plt.show()
"""