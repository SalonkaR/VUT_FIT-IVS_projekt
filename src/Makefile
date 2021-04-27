# Makefile

##
# @file Makefile

NAME = xhorni20_xtvaro00_xbrnaf00_xsokol14

.PHONY:

all: 
	
test:
	python3 -m unittest tests/math/math_tester.py

profile: 
	python3 profiling.py

run:
	python3 main.py

doc: Doxyfile clean-doc
	cd .. && mkdir doc && cd doc && doxygen ../src/Doxyfile

clean:
	cd .. && rm -rf $(NAME).zip
	cd ../../ && rm -rf $(NAME)
	rm -rf dist/*

clean-doc:
	cd .. && rm -rf doc dist

pack: doc
	rm -rf __pycache__
	mkdir ../../$(NAME)
	mkdir ../../$(NAME)/repo && cp -r ../../ivs_projekt/. ../../$(NAME)/repo
	mkdir ../../$(NAME)/installer && cp -f -r dist/. ../../$(NAME)/installer
	mkdir ../../$(NAME)/doc && cp -r ../doc/. ../../$(NAME)/doc
	cd ../../$(NAME) && zip -r $(NAME).zip repo installer doc

installer: req
	pyinstaller --onefile main.py
	rm -rf build
	rm -f main.spec

req: requirements.txt
	sudo apt-get install python-setuptools
	sudo apt install python3-pip
	pip3 install -r requirements.txt