TOPICS=de pr stats

topics:
	for d in $(TOPICS); do \
			$(MAKE) -C $$d; \
	done

%.pdf: topics
	cp $*/$*.pdf ./
