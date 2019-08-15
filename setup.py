from setuptools import setup
import sphinx_heigvd_theme
with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='sphinx_heigvd_theme',
    version='0.5.1',
    url='https://github.com/heig-vd-tin/sphinx-heigvd-theme',
    license='MIT',
    author='Yves Chevallier <yves.chevallier@heig-vd.ch>',
    description='A Sphinx-doc theme based on sphinx press theme',
    long_description = long_description,
    packages=['sphinx_heigvd_theme'],
    package_data={'sphinx_heigvd_theme': [
        'theme.conf',
        '*.html',
        'util/*.html',
        'static/*.css',
        'static/*.js',
        'static/*.ico'
    ]},
    entry_points = {
        'sphinx.html_themes': [
            'heigvd = sphinx_heigvd_theme',
        ]
    },
    install_requires=[
       'sphinx >= 2.0.0'
    ],
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
    keywords = "sphinx doc theme heig-vd vue.js",
    project_urls = {
        'Source': 'https://github.com/heig-vd-tin/sphinx-heigvd-theme',
        'Tracker': 'https://github.com/heig-vd-tin/sphinx-heigvd-theme/issues',
    },
)
