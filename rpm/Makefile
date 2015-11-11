COMMIT := $(shell git rev-parse HEAD)
SHORTCOMMIT := $(shell git rev-parse HEAD|cut -c-7)
TEMPDIR := $(shell mktemp -d)

build_rpm:
	git archive --format=tar.gz --prefix webhook-$(COMMIT)/ --output $(TEMPDIR)/webhook-$(SHORTCOMMIT).tar.gz $(COMMIT)
	rpmbuild -ta --define "_commit $(COMMIT)" $(TEMPDIR)/webhook-$(SHORTCOMMIT).tar.gz
