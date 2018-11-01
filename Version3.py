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

fact_scale = input("Is scale a facotr? [yes or no]")
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
pass_scale = np.around(thick_scale/pd_scale,decimals=1)            #Number of passes for scale
pass_rough = np.around(thick_rough/pd_rough,decimals=1)            #Number of passes for roughing
pass_finish = np.around(thick_finish/pd_finish,decimals=1)         #Number of passes for finishing
pass_total = np.around(pass_scale+pass_rough+pd_finish,decimals=1) #Total number of passes required

"""ANALYSIS CALCULATIONS"""
total = pass_total.item(wh)/pass_total.item(op)
if total < 1:
    total_per = int(total*100)
    total_str = "Wheel is underutilized across operation"
if total == 1:
    total_per = int(total*100)
    total_str = "Wheel is utilized correctly across operation"
if total > 1:
    total_per = int(total*100)
    total_str = "Wheel us overutilized across operation"

total_scale = pass_scale.item(wh)/pass_scale.item(op)
if total_scale < 1:
    total_per_scale = int(total_scale*100)
    total_str_scale = "Wheel underutilized in scale region"
if total_scale == 1.0:
    total_per_scale = int(total_scale*100)
    total_str_scale = "Wheel utilized correctly in scale region"
if total_scale > 1:
    total_per_scale = int(total_scale*100)
    total_str_scale = "Wheel overutilized in scale region"

total_rough = pass_rough.item(wh)/pass_rough.item(op)
if total_rough < 1:
    total_per_rough = int(total_rough*100)
    total_str_rough = "Wheel underutilized in roughing region"
if total_rough == 1.0:
    total_per_rough = int(total_rough*100)
    total_str_rough = "Wheel utilized correctly in roughing region"
if total_rough > 1:
    total_per_rough = int(total_rough*100)
    total_str_rough = "Wheel overutilized in roughing region"

total_finish = pass_finish.item(wh)/pass_finish.item(op)
if total_finish < 1:
    total_per_finish = int(total_finish*100)
    total_str_finish = "Wheel underutilized in finishing region"
if total_finish == 1.0:
    total_per_finish = int(total_finish*100)
    total_str_finish = "Wheel utilized correctly in finishing region"
if total_finish > 1:
    total_per_finish = int(total_finish*100)
    total_str_finish = "Wheel overutilized in finishing region"

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
print(""*50)
print("WHEEL VS. OPERATOR COMPARISION")
print("-"*50)
print(total_str,"[",total_per,"% Capacity","]")
print(total_str_scale,"[",total_per_scale,"% Capacity","]")
print(total_str_rough,"[",total_per_rough,"% Capacity","]")


