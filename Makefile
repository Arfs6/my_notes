# My notes makefile
# Used for building latex files and such
#
TEX_FILES := $(shell find . -name '*.tex')
AUX_FILES := $(shell find . -name '*.aux' -o -name '*.lof' -o -name '*.log' -o -name '*.lot' -o -name '*.fls' -o -name '*.out' -o -name '*.toc' -o -name '*.fmt' -o -name '*.fot' -o -name '*.dvi' -o -name '*.xdv' -o -name '*.4ct' -o -name '*.4tc' -o -name '*.idv' -o -name '*.xref' -o -name '*.lg' -o -name '*.tmp')

all: $(TEX_FILES:.tex=.html)
	@echo $(TEX_FILES)
	@echo "Done."

%.html: %.tex
	@echo Compiling $<
	cd $(shell dirname $<) &&\
	make4ht -x -u $(shell basename $<) "html,frame,next,mathjax"

.PHONY:
clean:
	@echo "Removing auxilary files: ..."
	@$(foreach file, $(AUX_FILES), rm -f $(file);)
