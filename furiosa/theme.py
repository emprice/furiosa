from .colors import nord, _scale_lightness, _hexscale, _hexalpha

lighten = lambda hx: _hexscale(hx, 1.1)
darken  = lambda hx: _hexscale(hx, 0.9)

def _get_default_css_variables():

    css_common_defaults = {
        ### fonts ##############################################################
        'font-size--normal'   : r'100%',
        'font-size--small'    : r'95%',
        'font-size--small--2' : r'90%',
        'font-size--small--3' : r'85%',
        'font-size--small--4' : r'80%',
        'font-stack' : '\'Raleway\', sans-serif',
        'font-stack--monospace' : '\'Source Code Pro\', monospace',
        'admonition-font-size' : '1rem',
        'admonition-title-font-size' : '1rem',

        ### admonition colors ##################################################
        'color-topic-title' : nord.frost.greenish,
        'color-topic-title-background' :
            _hexalpha(nord.frost.greenish, 0.3),
        'color-admonition-title' : nord.aurora.purple,
        'color-admonition-title-background' :
            _hexalpha(nord.aurora.purple, 0.3),
        'color-admonition-title--admonition-todo' : nord.aurora.purple,
        'color-admonition-title-background--admonition-todo' :
            _hexalpha(nord.aurora.purple, 0.3),
        'color-admonition-title--caution' : nord.aurora.yellow,
        'color-admonition-title-background--caution' :
            _hexalpha(nord.aurora.yellow, 0.3),
        'color-admonition-title--warning' : nord.aurora.orange,
        'color-admonition-title-background--warning' :
            _hexalpha(nord.aurora.orange, 0.3),
        'color-admonition-title--danger' : nord.aurora.red,
        'color-admonition-title-background--danger' :
            _hexalpha(nord.aurora.red, 0.3),
        'color-admonition-title--attention' : nord.aurora.red,
        'color-admonition-title-background--attention' :
            _hexalpha(nord.aurora.red, 0.3),
        'color-admonition-title--error' : nord.aurora.red,
        'color-admonition-title-background--error' :
            _hexalpha(nord.aurora.red, 0.3),
        'color-admonition-title--hint' : nord.aurora.green,
        'color-admonition-title-background--hint' :
            _hexalpha(nord.aurora.green, 0.3),
        'color-admonition-title--important' : nord.frost.greenish,
        'color-admonition-title-background--important' :
            _hexalpha(nord.frost.greenish, 0.3),
        'color-admonition-title--note' : nord.frost.light,
        'color-admonition-title-background--note' :
            _hexalpha(nord.frost.light, 0.3),
        'color-admonition-title--seealso' : nord.frost.med,
        'color-admonition-title-background--seealso' :
            _hexalpha(nord.frost.med, 0.3),
        'color-admonition-title--tip' : nord.aurora.green,
        'color-admonition-title-background--tip' :
            _hexalpha(nord.aurora.green, 0.3),
    }

    css_defaults = {
        'light_css_variables' : {
            'color-problematic' : nord.aurora.red,

            ### base colors ####################################################
            'color-foreground-primary' : nord.polar_night.darkest,
            'color-foreground-secondary' : nord.polar_night.darker,
            'color-background-primary' : lighten(nord.snow_storm.lightest),
            'color-background-secondary' : nord.snow_storm.lightest,

            ### announcements ##################################################
            'color-annoucnement-background' : nord.aurora.green,
            'color-annoucnement-text' : nord.snow_storm.lightest,

            ### brand colors ###################################################
            'color-brand-primary' : nord.frost.dark,
            'color-brand-content' : nord.frost.dark,

            ### highlight color ################################################
            'color-highlight-on-target' : nord.aurora.yellow,
            'color-highlighted-text' : nord.snow_storm.lightest,
            'color-highlighted-background' : nord.polar_night.med,

            ### table colors ###################################################
            'color-table-border' : darken(nord.snow_storm.light),
        },
        'dark_css_variables' : {
            'color-problematic' : nord.aurora.red,

            ### base colors ####################################################
            'color-foreground-primary' : nord.snow_storm.lightest,
            'color-foreground-secondary' : nord.snow_storm.lighter,
            'color-background-primary' : darken(nord.polar_night.darkest),
            'color-background-secondary' : nord.polar_night.darker,

            ### announcements ##################################################
            'color-annoucnement-background' : nord.aurora.green,
            'color-annoucnement-text' : nord.snow_storm.lightest,

            ### brand colors ###################################################
            'color-brand-primary' : nord.frost.light,
            'color-brand-content' : nord.frost.light,

            ### highlight color ################################################
            'color-highlight-on-target' : nord.aurora.orange,
            'color-highlighted-text' : nord.polar_night.darkest,
            'color-highlighted-background' : nord.aurora.yellow,

            ### table colors ###################################################
            'color-table-border' : _hexalpha(nord.snow_storm.light, 0.5),
        }
    }

    css_defaults['light_css_variables'].update(css_common_defaults)
    css_defaults['dark_css_variables'].update(css_common_defaults)

    return css_defaults

# vim: set ft=python:
