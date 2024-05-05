.PHONY: mypy
mypy:
	mypy infezione

.PHONY: clean
clean:
	$(RM) -r dist
	$(RM) -r pypi
	$(RM) setup.py
	$(RM) pyproject.toml
	$(RM) -r infezione.egg-info

.PHONY: upload
upload: pypi
	twine upload --username __token__ --password `cat .token` pypi/*

pypi: setup.py infezione
	mkdir -p dist pypi
	./setup.py sdist
	./setup.py bdist_wheel
	mv dist/infezione-`head -1 CHANGELOG.md`.tar.gz pypi
	mv dist/*whl pypi
	rmdir dist
	gpg --detach-sign -a pypi/infezione-`head -1 CHANGELOG.md`.tar.gz
	gpg --detach-sign -a pypi/infezione-`head -1 CHANGELOG.md`-py3-none-any.whl

pyproject.toml: CHANGELOG.md
	./gensetup.py --$@

setup.py: CHANGELOG.md README.md
	./gensetup.py --$@
	chmod u+x setup.py
