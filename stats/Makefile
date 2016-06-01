all: stats.pdf stats.cheatsheet.pdf

stats.pdf: stats.tex */*.tex toc
	xelatex stats.tex

stats.cheatsheet.pdf: stats.cheatsheet.tex */*.tex toc
	xelatex stats.cheatsheet.tex

toc: */*.tex
	xelatex stats.tex
