import colorsys
import webcolors
from collections import namedtuple

polar_night = ['#2e3440', '#3b4252', '#434c5e', '#4c566a']
snow_storm = ['#d8dee9', '#e5e9f0', '#eceff4']
frost = ['#8fbcbb', '#88c0d0', '#81a1c1', '#5e81ac']
aurora = ['#bf616a', '#d08770', '#ebcb8b', '#a3be8c', '#b48ead']

Nord = namedtuple('Nord', ['polar_night', 'snow_storm', 'frost', 'aurora'])
PolarNight = namedtuple('PolarNight', ['darkest', 'darker', 'dark', 'med'])
SnowStorm = namedtuple('SnowStorm', ['light', 'lighter', 'lightest'])
Frost = namedtuple('Frost', ['greenish', 'light', 'med', 'dark'])
Aurora = namedtuple('Aurora', ['red', 'orange', 'yellow', 'green', 'purple'])

spec1 = PolarNight(*polar_night)
spec2 = SnowStorm(*snow_storm)
spec3 = Frost(*frost)
spec4 = Aurora(*aurora)

nord = Nord(spec1, spec2, spec3, spec4)

def _scale_lightness(rgb, scale):
    ''' https://stackoverflow.com/a/60562502/1552418 '''
    # convert rgb to hls
    h, l, s = colorsys.rgb_to_hls(*rgb)
    # manipulate h, l, s values and return as rgb
    return colorsys.hls_to_rgb(h, min(1, l * scale), s=s)

def _hexscale(hexcode, scale):
    rgb = webcolors.hex_to_rgb(hexcode)
    rgb = tuple(map(lambda x: x / 255, rgb))
    scaled = _scale_lightness(rgb, scale)
    scaled = tuple(map(lambda x: int(x * 255), scaled))
    return webcolors.rgb_to_hex(scaled)

def _hexalpha(hexcode, alpha):
    r, g, b = webcolors.hex_to_rgb(hexcode)
    return f'rgba({r}, {g}, {b}, {alpha})'

# vim: set ft=python:
