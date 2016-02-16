CC=./makepdf.py

all: pr.pdf de.pdf pr.exam.pdf de.exam.pdf

pr.pdf: pr/includes/* pr/lectures/* pr/questions/* pr/cards/* pr/cheatsheets/*
	$(CC) pr/includes pr/lectures pr/questions pr/cards pr/cheatsheets
	cp out/out.pdf pr.pdf

de.pdf: de/includes/* de/lectures/* de/questions
	$(CC) de/includes de/lectures de/questions
	cp out/out.pdf de.pdf
