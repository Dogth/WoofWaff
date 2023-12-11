from params import *
from colour import XYZ_to_RGB, RGB_to_XYZ
from matplotlib.colors import to_rgb, to_hex

def XYZ_RGB(XYZ_color,
            Colorspace=RGB_COLORSPACE,
            Illuminant=ILLUMINANT,
            Transform=RGB_TRANSFORM):
    return XYZ_to_RGB(XYZ_color,
                      Colorspace,
                      Illuminant,
                      Transform,
                      True
                      ).clip(0,1)

def RGB_XYZ(RGB_color, 
            Colorspace=RGB_COLORSPACE,
            Illuminant=ILLUMINANT,
            Transform=RGB_TRANSFORM):
    return RGB_to_XYZ(RGB_color,
                      Colorspace, 
                      Illuminant,
                      Transform,
                      True
                      ).clip(0,1)

def XYZ_HEX(XYZ_color,
            Colorspace=RGB_COLORSPACE,
            Illuminant=ILLUMINANT,
            Transform=RGB_TRANSFORM):
    return to_hex(XYZ_RGB(XYZ_color,
                          Colorspace,
                          Illuminant,
                          Transform))

def HEX_XYZ(HEX_color,
            Colorspace=RGB_COLORSPACE,
            Illuminant=ILLUMINANT, 
            Transform=RGB_TRANSFORM):
    return RGB_XYZ(HEX_RGB(HEX_color),
                   Colorspace, 
                   Illuminant, 
                   Transform)

def RGB_HEX(RGB_color):
    return to_hex(RGB_color)

def HEX_RGB(HEX_color):
    return to_rgb(HEX_color)
