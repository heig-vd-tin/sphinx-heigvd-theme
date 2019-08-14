# Sphinx HEIG-VD Theme

[![Build Status](https://travis-ci.org/heig-vd-tin/sphinx-heigvd-theme.svg?branch=master)](https://travis-ci.org/heig-vd-tin/sphinx-heigvd-theme)

This theme is a fork of the [sphinx-press-theme](https://schettino72.github.io/sphinx_press_site/)
based on [VuePress](https://vuepress.vuejs.org/). It uses [Vue.js](https://vuejs.org/) & [Stylus](http://stylus-lang.com/)
managed by [webpack](https://webpack.js.org/) (through [vue-cli](https://cli.vuejs.org/)).

## Installation

First install the theme:

```
$ pip install git+https://github.com/heig-vd-tin/sphinx-heigvd-theme
```

On Sphinx project's ``conf.py``: set the theme name to ``heigvd``.

```
html_theme = "heigvd"
```

See details on [Sphinx theming docs](http://www.sphinx-doc.org/en/master/theming.html#using-a-theme).

## Development

To contribute to this theme you should first build the web assets:

```
cd ui
npm run build
```

Sphinx theme has a soft link to built assets. Once done, install the theme locally
with `pip install -e .`.

`docs` folder contains theme's own documentantion.

```
cd docs
make clean; make html
```
