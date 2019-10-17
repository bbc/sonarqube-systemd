PHONY: prepare build

ifndef VERSION
$(error VERSION must be specified)
endif

prepare:
	rm -rf BUILD RPMS SRPMS BUILDROOT tmp
	curl https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-$(VERSION).zip -o SOURCES/sonarqube-$(VERSION).zip

build:
	rpmbuild -bb --define="_topdir $(PWD)" --define="ver $(VERSION)" --define="_tmppath $(PWD)/tmp" SPECS/sonarqube.spec
	cp -r RPMS/* repo/
	createrepo repo -s sha
