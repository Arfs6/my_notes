# My notes makefile
# Used for building latex files and such
#
TEX_FILES := $(shell find . -name '*.tex')
INDEX_FILES = $(shell find . -name 'index.tex')
AUX_FILES := $(shell find . -name '*.aux' -o -name '*.lof' -o -name '*.log' -o -name '*.lot' -o -name '*.fls' -o -name '*.out' -o -name '*.toc' -o -name '*.fmt' -o -name '*.fot' -o -name '*.dvi' -o -name '*.xdv' -o -name '*.4ct' -o -name '*.4tc' -o -name '*.idv' -o -name '*.xref' -o -name '*.lg' -o -name '*.tmp')

.PHONY: all
all: $(TEX_FILES:.tex=.html)
	@echo adding list to index files ...
	@$(foreach file, $(INDEX_FILES), ./scripts/add_listing.py $(file); echo $(file);)
	@echo "Done."

%.html: %.tex
	@echo Compiling $<
	cd $(dir $<) &&\
	make4ht -x -u $(notdir $<) "html,frame,next,mathjax"

.PHONY: clean
clean:
	@echo "Removing auxilary files: ..."
	@$(foreach file, $(AUX_FILES), rm -f $(file);)
