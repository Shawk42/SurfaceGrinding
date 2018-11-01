import numpy as np
'''
This is a second more analytical attempt at the same problem
All dimensions are in inches
'''

"""MATERIAL PROPERTIES"""
#User Inputs
height = .25             #Initial height of the material
finish = .125            #Finished height of the material

"""PROCESS INPUTS"""
#User Inputs
thick_finish = .003    #With how many thou left with operator start finishing pass
op_pd_scale = .003     #How deep of a pass is the operator taking through scale
pd_scale = .003        #How deep of a pass can the wheel take through scale
op_pd_rough = .004     #How deep of a pass is the operator taking through roughing
pd_rough = .005        #How deep of a pass can the wheel taking while roughing
op_pd_finish = .002    #How deep of a pass is the operator taking while finishing
pd_finish = .002       #How deep of a pass can the wheel take while roughing
fact_scale = input("Is scale a factor? [yes or no]")
if fact_scale == "yes":
    print("Scale was considered")
    thick_scale = .0039       #Typical to max depth of scale
else:
    print("Scale was not considered")
    thick_scale = 0           #Scale still needs to be defined

#Calculated Inputs
delta = height-finish                               #Total material to be removed
thick_rough = delta-thick_finish-thick_scale
thick_check = thick_rough+finish
dev1 = np.absolute(height-thick_check)
if dev1 >= .0001:
    print("Thickness calulcation error")
    print("Deviation",dev1)
    print("Inputted height",height)
    print("Caclulated height",thick_check)



