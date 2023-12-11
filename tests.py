import unittest
import numpy as np

from numpy.testing import *
from utils import *
from params import *
from transforms import *

D65_ILLUMINANT = [0.3127, 0.329]

### Colors ### 
colors = [
color(
    [0, 0, 0],
    [0, 0, 0],
    '#000000'
),
color(
    [0.5011    , 0.4005    , 0.3019    ],
    [0.93463086, 0.56412275, 0.55199771],
    '#ee908d'
),
color(
    [0.2551  , 0.4005    , 0.1110    ],
    [0.431068, 0.74105054, 0.24742867],
    '#6ebd3f'
),
color(
    [0.3847    , 0.4005    , 0.9323   ],
    [0.44443819, 0.67793339, 0.9664219],
    '#71adf6'
)
]
### Tests ###

class Test(unittest.TestCase):
    def test_XYZ_RGB(self):
        for color in colors:
            assert_allclose(
                XYZ_RGB(color.XYZ, Illuminant=D65_ILLUMINANT),
                color.RGB,
                atol=0.001)

    def test_RGB_XYZ(self):
        for color in colors:
            assert_allclose(
                RGB_XYZ(color.RGB, Illuminant=D65_ILLUMINANT),
                color.XYZ,
                atol=0.001)

    def test_XYZ_HEX(self):
        for color in colors:
            self.assertEqual(
                XYZ_HEX(color.XYZ, Illuminant=D65_ILLUMINANT),
                color.HEX)

    def test_RGB_HEX(self):
        for color in colors:
            self.assertEqual(
                RGB_HEX(color.RGB),
                color.HEX)

    def test_HEX_XYZ(self):
        for color in colors:
            assert_allclose(
                HEX_XYZ(color.HEX, Illuminant=D65_ILLUMINANT),
                color.XYZ,
                atol=0.01)

    def test_HEX_RGB(self):
        for color in colors:
            assert_allclose(
                HEX_RGB(color.HEX),
                color.RGB,
                atol=0.01)

if __name__ == '__main__':
    unittest.main()
