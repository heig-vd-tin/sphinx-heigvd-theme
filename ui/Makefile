
all: init build

build:
	npm run build

init:
	npm install

deploy:
	cp -f dist/favicon.ico ../sphinx_heigvd_theme/static/favicon.ico
	cp -f dist/heig-vd.svg ../sphinx_heigvd_theme/static/heig-vd.svg
	cp -f dist/js/chunk-vendors.js ../sphinx_heigvd_theme/static/theme-vendors.js
	cp -f dist/css/app.css ../sphinx_heigvd_theme/static/theme.css
	cp -f dist/js/app.js ../sphinx_heigvd_theme/static/theme.js

clean:
	$(RM) -rf dist

distclean:
	$(RM) -rf node_modules

.PHONY: all init build deploy
