CC=./makepdf.py

all: pr.pdf de.pdf pr.exam.pdf de.exam.pdf

pr.pdf: pr/includes/* pr/lectures/*
	$(CC) pr/includes pr/lectures
	cp out/out.pdf pr.pdf

de.pdf: de/includes/* de/lectures/*
	$(CC) de/includes de/lectures
	cp out/out.pdf de.pdf

pr.exam.pdf: pr.exam.notes/includes/* pr.exam.notes/questions/* pr.exam.notes/cards/*
	$(CC) pr.exam.notes/includes pr.exam.notes/questions pr.exam.notes/cards
	cp out/out.pdf pr.exam.pdf

de.exam.pdf: de.exam.notes/includes/* de.exam.notes/questions/*
	$(CC) de.exam.notes/includes de.exam.notes/questions
	cp out/out.pdf de.exam.pdf
