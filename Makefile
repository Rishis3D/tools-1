#-----------------------------------------------------------------------------#
#
# Greetings!
#
# This Makefile was generated by `package`, the Python package package
# package. If you don't know what that means, that's OK. This Makefile is
# mostly for the "author" of this package. If you are not the author you can
# ignore this file, or you can use it to call the setup.py commands that you
# are used to:
#
# * make build
# * make test
# * sudo make install
#
# If you are the module author, you can run `make help` to see all the
# commands that are available to you.
#
# This Makefile currently assumes that, if you are the package author, you are
# on some kind of Unix based system.
#
# For more information on the Python package package package, `package`, visit
# the Python Package Index here:
#
#     http://pypi.python.org/pypi/bcTools/
#
# Cheers!
#
#-----------------------------------------------------------------------------#

.PHONY: \
    help \
    build \
    test \
    tests \
    install \
    register \
    sdist \
    clean \
    purge \
    upload \

# This variable is hardcoded into the Makefile by initial setup.
# If you move package-py, you need to change this.
PACKAGE_BASE = $(MAKEFILE_LIST:%/Makefile=%)

PYTHON = python

ALL_TESTS = $(shell echo tests/*.py)

#-----------------------------------------------------------------------------#
# package-py targets
#-----------------------------------------------------------------------------#
help::
	@echo "This is the package (Python package package package) Makefile."
	@echo ""
	@echo "These targets are simply run by your setup.py:"
	@echo ""
	@echo "* build - Compile the Python modules"
	@echo "* test - Run the unittests"
	@echo "* nosetests - Run the unittests"
	@echo "* register - Register this package to PyPi"
	@echo "* sdist - Create a dist bundle file"
	@echo "* upload - Create the dist bundle and upload it to PyPi"
	@echo "* clean - Remove the various generated files"

#-----------------------------------------------------------------------------#
# setup.py targets
#-----------------------------------------------------------------------------#
build nosetests devtest install register sdist clean::
	$(PYTHON) setup.py $@

upload::
	$(PYTHON) setup.py sdist bdist_egg bdist_wheel $@

test:: nosetests

nosetests:: $(ALL_TESTS)

$(ALL_TESTS):
	@$(PYTHON) -c 'print " Running test: $@ ".center(70, "-") + "\n"'
	@PYTHONPATH=. $(PYTHON) $@

clean::
	rm -fr build dist MANIFEST cover *.egg-info
	find . -name '*.pyc' | xargs rm

purge:: clean

#-----------------------------------------------------------------------------#
# Git Targets targets
#-----------------------------------------------------------------------------#
pushtag:
	git tag $@
	git push --tags
