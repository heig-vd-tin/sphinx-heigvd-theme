all: build install demo

demo:
	$(MAKE) -C demo html

build:
	$(MAKE) -C ui
	cp --remove-destination ui/public/favicon.ico sphinx_heigvd_theme/static
	cp --remove-destination ui/public/heig-vd.svg sphinx_heigvd_theme/static
	cp --remove-destination ui/dist/js/chunk-vendors.js sphinx_heigvd_theme/static
	cp --remove-destination ui/dist/css/app.css sphinx_heigvd_theme/static
	cp --remove-destination ui/dist/js/app.js sphinx_heigvd_theme/static

install:
	pip install -e .

dist: build
	python3 setup.py sdist --formats=gztar,zip

.PHONY: all build install demo