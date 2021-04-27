# Makefile

##
# @file Makefile

ZIP_NAME = xhorni20_xtvaro00_xbrnaf00_xsokol14.zip

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
	cd .. && rm -rf $(ZIP_NAME)

clean-doc:
	cd .. && rm -rf doc

pack: doc
	rm -rf __pycache__
	cd .. && zip -r $(ZIP_NAME) *
