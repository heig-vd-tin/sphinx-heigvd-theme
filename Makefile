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

dist:
	python3 setup.py sdist bdist_wheel

.PHONY: all build install demo