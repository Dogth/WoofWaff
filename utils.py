import pylab
import colour
import numpy as np
import matplotlib.pyplot as plt
from colour.plotting import *
from params import *
from transforms import *

class color:
    def __init__(self, XYZ, RGB, HEX):
        self.XYZ = np.array(XYZ)
        self.RGB = np.array(RGB)
        self.HEX = HEX

    def from_XYZ(XYZ, Illuminant=ILLUMINANT):
        return color(XYZ, 
                     XYZ_RGB(XYZ, Illuminant=Illuminant),
                     XYZ_HEX(XYZ, Illuminant=Illuminant))
    
    def from_Hellwig2022( #TODO: READ THE DOCUMENTATION
            chroma,hue, #TODO: TF IS THIS?
            hue_quadrature, #ANGLE
            hue_composition, #TODO: HUH?
            
            Lightness=LIGHTNESS,
            Saturation=SATURATION,
            Brightness=BRIGHTNESS,
            Colorfullness=COLORFULLNESS,
            
            JHK=0,
            QHK=0):
        spec = colour.appearance.CAM_Specification_Hellwig2022(
                C=chroma,
                h=hue,
                H=hue_quadrature,
                HC=hue_composition,
                J=Lightness,
                s=Saturation,
                Q=Brightness,
                M=Colorfullness,
                J_HK=JHK,
                Q_HK=QHK
            )
        return color.from_XYZ(
            colour.appearance.Hellwig2022_to_XYZ(
                spec,XYZ_W,L_A,Y_B,HELLWIG2022_INDUCTION)/100
        )
        

def make_plot(XYZ_colors):
    plot_RGB_colourspaces_in_chromaticity_diagram_CIE1931(
        ['DCI-P3', 'sRGB', budget_display_colorspace],
        show = False,
        show_whitepoints = False,
        show_diagram_colours = False
    )
    
    ### Colorblindness copoints ###
    plot_point(prot_copoint, '#FF0000'  )
    plot_point(deut_copoint, '#0000FF' )
    plot_point(trit_copoint, '#00FF00'   )
    
    for color in XYZ_colors:
        plot_point(colour.XYZ_to_xy(color.XYZ), color.HEX)
    
#    plot_RGB_scatter(
#        get_attributes(XYZ_colors, 'XYZ'),
#        'sRGB',
#        'CIE XYZ',
#        show = False,
#        show_grid = False,
#        show_spectral_locus = True
#    )

def plot_point(coords,
               color='#000000', 
               annotation=None,
               offset=(0,0)):
    pylab.plot(coords[0],coords[1], 'o', color=color)
    
    if annotation:
        pylab.annotate(
            annotation,
            (x,y),
            offset,
            textcoords='offset points',
            xytext=(0,0),
            ha='center',
            va='center'
        )

def r_luminance_RGB(color):
    primaries = [
        ((col + 0.055) / 1.055) ** 2.4  
        if col >= 0.03928 else 
        col / 12.92 
        for col in color
    ]
    return 0.2126 * primaries[0] + 0.7152 * primaries[1] + 0.0722 * primaries[2]

def contrast_ratio_RGB(fg, bg=XYZ_RGB(BACKGROUND)):
    return (r_luminance_RGB(fg) + 0.05) / (r_luminance_RGB(bg) + 0.05)

def deltaE(color1, color2):
    return colour.delta_E(color1, color2, method='CIE 2000')

def get_attributes(objects, atribute):
    return np.array([getattr(obj, atribute) for obj in objects])

