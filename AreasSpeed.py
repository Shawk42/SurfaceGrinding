'''
The purpose of this section of code is to calculate the time required based off volumes and speeds. The general idea is that
this code could be combined with Version3 to predict the time required based off wheel and operator. Currently the code
assumes that the pieces loaded next to each other.
'''

"""INPUTS"""
V_raw = 2               #Velocity in [ft/s]
Wheel_width = 5         #Width of the wheel [in]
Wheel_travel = 2        #Amount of wheel overtravel per side
Stick_width = 2         #Width of an individual workpiece
Stick_length = 100      #Length of individual workpieces
Sticks = 8              #Number of sticks

"""UNIT CONVERSION"""
V = V_raw*12         #Coverting ft/s to in/s

"""WORKPIECE AREA CALCULATIONS"""
Area_inv = Stick_width*Stick_length  #Area of an indvidual stick
Area = Area_inv*Sticks               #Total workpiece area

"""WHEEL AREA CACLULATIONS"""
Wheel_length = Stick_length+(2*Wheel_travel)
Area_wh = Wheel_length*Wheel_width



