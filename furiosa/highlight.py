from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Punctuation, Generic
from .colors import nord, _scale_lightness, _hexscale, _hexalpha

nd_lighten = lambda hx: _hexscale(hx, 1.2)
nd_darken  = lambda hx: _hexscale(hx, 0.9)

class NordDark(Style):
    default_style = ''
    background_color = nord.polar_night.darker
    highlight_color = nd_lighten(nord.polar_night.dark)
    styles = {
        Generic :                nord.snow_storm.lightest,
        Punctuation :            nord.snow_storm.lightest,
        Operator :               nord.snow_storm.lightest,
        Comment :                'italic ' + nord.snow_storm.light,
        Comment.Preproc :        'bold noitalic ' + nord.aurora.purple,
        Comment.PreprocFile :    'nobold noitalic ' + nord.aurora.purple,
        Keyword :                'bold ' + nord.frost.light,
        Operator.Word :          nord.frost.light,
        Number :                 nd_darken(nord.aurora.purple),
        Name :                   nord.snow_storm.lightest,
        Name.Builtin :           'bold ' + nord.frost.light,
        Name.Constant :          nord.aurora.red,
        Name.Function :          nord.frost.greenish,
        Name.Class :             nord.frost.greenish,
        Name.Namespace :         nord.aurora.yellow,
        String :                 nd_darken(nord.aurora.green),
        String.Escape :          nd_darken(nord.aurora.orange),
    }

nl_lighten = lambda hx: _hexscale(hx, 1.1)
nl_darken  = lambda hx: _hexscale(hx, 0.7)

class NordLight(Style):
    default_style = ''
    background_color = nord.snow_storm.lightest
    highlight_color = _hexalpha(nl_lighten(nord.aurora.yellow), 0.5)
    styles = {
        Generic :                nord.polar_night.darkest,
        Punctuation :            nord.polar_night.darkest,
        Operator :               nord.polar_night.darkest,
        Comment :                'italic ' + nord.polar_night.med,
        Comment.Preproc :        'bold noitalic ' + nl_darken(nord.aurora.purple),
        Comment.PreprocFile :    'nobold noitalic ' + nl_darken(nord.aurora.purple),
        Keyword :                nord.frost.dark,
        Operator.Word :          nord.frost.dark,
        Number :                 nl_darken(nord.aurora.purple),
        Name :                   nord.polar_night.darkest,
        Name.Builtin :           'bold  ' + nord.frost.dark,
        Name.Constant :          nord.aurora.red,
        Name.Function :          nord.frost.greenish,
        Name.Class :             nord.frost.greenish,
        Name.Namespace :         nl_darken(nord.aurora.yellow),
        String :                 nl_darken(nord.aurora.green),
        String.Escape :          nl_darken(nord.aurora.orange),
    }

# vim: set ft=python:
