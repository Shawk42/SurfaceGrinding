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
wh_pd_scale = .003        #How deep of a pass can the wheel take through scale

op_pd_rough = .004     #How deep of a pass is the operator taking through roughing
wh_pd_rough = .005        #How deep of a pass can the wheel taking while roughing

op_pd_finish = .002    #How deep of a pass is the operator taking while finishing
wh_pd_finish = .002       #How deep of a pass can the wheel take while roughing

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
thick_check = thick_rough+thick_scale+thick_finish+finish
dev1 = np.absolute(height-thick_check)
if dev1 >= .0001:                             #Logic statement that prints thickness error
    print("Thickness calulcation error")
    print("Deviation",dev1)
    print("Inputted height",height)
    print("Caclulated height",thick_check)

"""MATRIX CREATION"""
op = 0           #index for operator
wh = 1           #index for wheel limit
pd_scale = np.array([op_pd_scale,wh_pd_scale])    #Array of scale pass depth
pd_rough = np.array([op_pd_rough,wh_pd_rough])    #Array of roughing pass depth
pd_finish = np.array([op_pd_finish,wh_pd_finish]) #Array of finishing pass depth

"""PASS CALCULATIONS"""
pass_scale = thick_scale/pd_scale            #Number of passes for scale
pass_rough = thick_rough/pd_rough            #Number of passes for roughing
pass_finish = thick_finish/pd_finish         #Number of passes for finishing
pass_total = pass_scale+pass_rough+pd_finish #Total number of passes required

"""ANALYSIS CALCULATIONS"""


"""PRINTING"""
print(""*50)
print("OPERATOR LIMITED PASSES")
print("-"*50)
print("Scale passes",pass_scale.item(op))
print("Roughing passes",pass_rough.item(op))
print("Finishing passes",pass_finish.item(op))
print(""*50)
print("WHEEL LIMITED PASSES")
print("-"*50)
print("Scale passes",pass_scale.item(wh))
print("Roughing passes",pass_rough.item(wh))
print("Finishing passes",pass_finish.item(wh))



