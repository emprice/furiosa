_furiosa_: A Nord twist on the Sphinx _furo_ theme
==================================================

 + [Building and installing](#nut_and_bolt-building-and-installing)
 + [Credits and dependencies](#gem-credits-and-dependencies)

# :nut_and_bolt: Building and installing

To build and install this package with `pip`, the same procedure can be
followed as for most pure Python packages that use `setuptools`. In the
install step, some optional flags are given below in brackets that can be
useful for a non-root build (`--user`) or for active development
(`--ignore-installed --force-reinstall`), but these are not strictly
necessary to install the package itself.

```
python3 -m build
pip3 install [--user] [--ignore-installed --force-reinstall] dist/furiosa-<version>.whl
```

To build the demo, the command below should be sufficient.

```
sphinx-build -M html demo <output dir>
```

# :gem: Credits and dependencies

 + [Furo](https://github.com/pradyunsg/furo) is the theme upon which this
   customization is based. Credit for its development goes entirely to
   [@pradyunsg](https://github.com/pradyunsg), and parts of my code that
   override bits of Furo are based on their code as well.
 + The [Nord](https://www.nordtheme.com) colorscheme is a beautiful set
   of color palettes with a frosty blue feel. I love these colors and use them
   in many places, not just documentation.
 + This extension additionally depends on
   [Sphinx](https://www.sphinx-doc.org/en/master),
   [Pygments](https://pygments.org), and
   [webcolors](https://webcolors.readthedocs.io/en/1.12). Everything else
   is included in the Python standard library.

<!-- vim: set ft=markdown: -->
