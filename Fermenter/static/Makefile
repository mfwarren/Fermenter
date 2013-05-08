STYLE= ./css/style.css
STYLE_MIN = ./css/style.min.css
STYLE_LESS = ./less/root.less
DATE=$(shell date +%I:%M%p)
CHECK=\033[32m✔\033[39m
HR=\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#


#
# BUILD DOCS
#

build:
	@echo "\n${HR}"
	@echo "Building CSS File..."
	@echo "${HR}\n"
	@./node_modules/.bin/recess --compile ${STYLE_LESS} > ${STYLE}
	@./node_modules/.bin/recess --compress ${STYLE_LESS} > ${STYLE_MIN}
	@echo "Compiling LESS with Recess...               ${CHECK} Done"
	@echo "\n${HR}"
	@echo "CSS successfully built at ${DATE}."
	@echo "${HR}\n"

#
# CLEANS THE ROOT DIRECTORY OF PRIOR BUILDS
#

clean:
	rm -r css/*.css

css: style-css
#
# CSS COMPLILE
#

style-css: css/*.css

css/*.css: less/*.less
	mkdir -p css
	./node_modules/.bin/recess --compile ${STYLE_LESS} > css/style.css
	./node_modules/.bin/recess --compress ${STYLE_LESS} > css/style.min.css

#
# WATCH LESS FILES
#

watch:
	echo "Watching less files..."; \
	watchr less.watchr


.PHONY: watch STYLE-css
