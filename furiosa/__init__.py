__version__ = '2023.05.02.dev1'

import os
from furo import _html_page_context, _builder_inited, \
    WrapTableAndMathInAContainerTransform
from pygments.formatters import HtmlFormatter

from .theme import _get_default_css_variables

def _config_inited(app, config):
    css_variables = _get_default_css_variables()
    useropts = config['html_theme_options']
    config['html_theme_options'] = css_variables

    for k in ['light_css_variables', 'dark_css_variables']:
        if k not in useropts.keys(): continue
        config['html_theme_options'][k].update(useropts[k])

def _builder_inited_wrapper(app):
    prev_theme = app.config.html_theme
    app.config.html_theme = 'furo'
    _builder_inited(app)
    app.config.html_theme = prev_theme

def _html_page_context_wrapper(app, pagename, templatename, context, doctree):
    prev_theme = app.config.html_theme
    app.config.html_theme = 'furo'
    _html_page_context(app, pagename, templatename, context, doctree)
    app.config.html_theme = prev_theme

def _get_pygments_styles(formatter, prefix):
    ''' https://github.com/pradyunsg/furo/blob/main/src/furo/__init__.py#L319 '''
    for line in formatter.get_linenos_style_defs():
        yield f'{prefix} {line}'
    yield from formatter.get_background_style_defs(prefix)
    yield from formatter.get_token_style_defs(prefix)

def _overwrite_pygments_css(app, exception):
    if exception is not None: return

    light_formatter = HtmlFormatter(style=app.config.pygments_style)
    dark_formatter = HtmlFormatter(style=app.config.pygments_dark_style)

    lines = list()
    lines.extend(_get_pygments_styles(light_formatter, prefix='.sig'))
    lines.append('@media not print {')
    dark_prefix = 'body[data-theme=\'dark\'] .sig'
    lines.extend(_get_pygments_styles(dark_formatter, prefix=dark_prefix))
    not_light_prefix = 'body:not([data-theme=\'light\']) .sig'
    lines.append('@media (prefers-color-scheme: dark) {')
    lines.extend(_get_pygments_styles(dark_formatter, prefix=not_light_prefix))
    lines.append('}')
    lines.append('}')

    with open(os.path.join(app.builder.outdir, '_static', 'pygments.css'), 'w') as f:
        f.write('\n'.join(lines))

def setup(app):
    app.require_sphinx('3.0')

    themedir = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme('furiosa', themedir)

    app.add_post_transform(WrapTableAndMathInAContainerTransform)

    app.connect('config-inited',     _config_inited)
    app.connect('builder-inited',    _builder_inited_wrapper)
    app.connect('html-page-context', _html_page_context_wrapper)
    app.connect('build-finished',    _overwrite_pygments_css)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
        'version': __version__,
    }

# vim: set ft=python:
