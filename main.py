#TODO: [ ] Implement contrast ratio calculation
#TODO: [ ] Implement deltaE calculation
#TODO: [ ] Implement deltaH calculation
#TODO: [ ] Implement deltaV calculation
#TODO: [ ] Implement revursive calculations
#TODO: [ ] Make sure colors fit in sRGB and 45% NTSC
#TODO: [ ] Cheap laptop display(45% NTSC) tristimulus
#TODO: [ ] Research color theory and cultural usage of colors
#TODO: [ ] Research colorblindness
#TODO: [ ] make sure colors are ratios are consistent
#TODO: Move to L'u'v

from utils import *

from params import *

import colour

z = [
    color.from_Hellwig2022(0,148.8,0,0),           #Green
    color.from_Hellwig2022(0,279.7,10,0),          #Blue
    color.from_Hellwig2022(0,41.2 ,0,0),           #Orange
    color.from_Hellwig2022(0,-18  ,0,0),           #Magenta
    color.from_Hellwig2022(10,205.6  ,10,10),      #Cyan
    color.from_Hellwig2022(0,6.2 ,0,0)             #Red
]


for col in z:
   print(contrast_ratio_RGB(col.RGB))
   print(col.HEX)
colors = [color.from_XYZ(col) for col in colorsXYZ]

colors.append(z)

vc = colour.appearance.VIEWING_CONDITIONS_HELLWIG2022

make_plot(z)

colour.plotting.render(
    show=True,
    limits=(-0.1,0.9,-0.1,0.9),
    x_tighten=True,
    y_tighten=True
)
