import colour
import numpy as np
from colour import Luv_uv_to_xy, xy_to_XYZ
from colour.appearance import InductionFactors_Hellwig2022

ILLUMINANT = [0.3422, 0.3502] #F11 ILLUMINANT
RGB_TRANSFORM = 'CAT02'
RGB_COLORSPACE = 'sRGB'
BACKGROUND = [0.013,0.014,0.015] #1F1F1F

LIGHTNESS     = 49.5
BRIGHTNESS    = 65
SATURATION    = 25.5
COLORFULLNESS = 42

XYZ_W = xy_to_XYZ(ILLUMINANT)*100
L_A = 120
Y_B = 5.2               #TODO:

HELLWIG2022_INDUCTION = InductionFactors_Hellwig2022(
    0.9, #max adaptation degree
    0.79, #exp non-linearity
    0.84, #chromatic induction
)

prot_copoint = (0.747, 0.253)
deut_copoint = (1.080,-0.800)
trit_copoint = (0.171, 0.000)

colorsXYZ = [
    [0.5011, 0.4005, 0.3019],
    [0.2551, 0.4005, 0.1110],
    [0.4495, 0.4005, 0.0682],
    [0.3847, 0.4005, 0.9323],
    [0.5507, 0.4005, 0.9681],
    [0.2477, 0.4005, 0.3752]
]

#Taken from NV156FHM-N42 45% NTSC TFT display datasheet (Typ.)
budget_display_primaries = np.array(
    [[0.590,0.350],[0.330,0.555],[0.153,0.119]]
)
budget_display_whitepoint = np.array([0.283,0.299])

budget_display_colorspace = colour.RGB_Colourspace(
    'Budget display panel gamut (approx.)',
    budget_display_primaries,
    budget_display_whitepoint,
    'B156HTN06'
)

#Hellwig 2022 specification

#Keep constant:
# 1) Lightness
# 2) Brightness
# 3) Saturation
# 4) colorfulness

specification = colour.appearance.CAM_Specification_Hellwig2022(
    J=41,#Lightneds
    C=40,#Chroma
    h=201,#hue angle
    s=40,#saturation 
    Q=40,#brightness
    M=120,#colorfulness
    H=1,#hue quadrature
    HC=1,#hue composition
    J_HK=1,#lighness w/ HK effect
    Q_HK=1 #brightness w/ HK effect
)

#Induction factors
#For dimly lit room with:
# 1) Yw = 140 cm/m^2
# 2) #1F1F1F background with 5% stuff
# 3) 50cm away from screen
# 4) Check for APCA
