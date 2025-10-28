TOP_DIR=$(CURDIR)/rpmbuild

build_rpm:
	rm -rf src
	git clone https://github.com/adnanh/webhook src
	cd src && \
		export VERSION=$$(git describe --tags --abbrev=0 | sed -e 's!v!!') && \
		export COMMIT=$$(git rev-parse HEAD) && \
		export SHORTCOMMIT=$$(git rev-parse HEAD|cut -c-7) && \
		export COMMIT_COUNT=$$(git rev-list --count HEAD) && \
		make build && \
		cd .. && \
		mkdir -p $(TOP_DIR)/ && \
		cp src/webhook $(TOP_DIR)/ && \
		cp src/hooks.json.example $(TOP_DIR)/ && \
		cp src/LICENSE $(TOP_DIR)/ && \
		cp src/README.md $(TOP_DIR)/ && \
		rpmbuild -bb \
			--define "_commit $$COMMIT" \
			--define "_shortcommit $$SHORTCOMMIT" \
			--define "_commitcount $$COMMIT_COUNT" \
			--define "_version $$VERSION" \
			--define "_topdir $(TOP_DIR)" \
			webhook.spec
	cp $(TOP_DIR)/RPMS/**/*.rpm .
	rm -rf $(TOP_DIR)

.PHONY: clean
clean:
	rm -rf *.rpm
	rm -rf src
	rm -rf $(TOP_DIR)
