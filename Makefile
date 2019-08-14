all: build install demo

demo:
	$(MAKE) -C demo html

build:
	$(MAKE) -C ui

install:
	pip install -e .

.PHONY: all build install demo