PANDOC=pandoc --latex-engine=xelatex -V mainfont='CMU Serif' -V geometry:margin=2cm -sS

all: de.lectures.pdf

de.lectures.pdf: 00 lectures/*.markdown
	find lectures -iname '*.markdown' -exec $(MAKE) \{\}.tex \;
	$(PANDOC) -o de.lectures.pdf 00 lectures/*.tex

%.tex: %.markdown
	pandoc -f markdown -t latex %.markdown -o %.tex

%.pdf: 00 %.markdown
	$(PANDOC) -o $*.pdf 00 $*.markdown

clean:
	ls de.lectures.pdf && rm de.lectures.pdf
	ls lectures/*.markdown.tex && rm lectures/*.markdown.tex
