Some basic tools that help your day to day life as an animation/VFX artist

:Author: `Barish Chandran B <http://www.barishcb.com>`_

.. contents::
    :local:
    :depth: 2
    :backlinks: none

.. sectnum::

Introduction
============

What is bcTools?
----------------

``bcTools`` conatins some basic tools for animation/VFX artists.

How is bcTools licensed?
------------------------

`MIT License <https://opensource.org/licenses/MIT>`_

Contact details
---------------

Drop me an email to barishcb@gmail.com for any questions regarding ``bcTools``. For reporting problems with ``bcTools`` or submitting feature requests, the best way is to open an issue on the `bcTools project page <https://github.com/barishcb/tools>`_.

Installation
============

Prerequisites
-------------

* ``bcTools`` was tested only on Python 2.7, on both Linux and Windows. It should work on any later version as well.

Installation process
--------------------

Installing ``bcTools`` is very simple. Once you download and unzip the package, you just have to execute the standard ``python setup.py install``. The setup script will then place the ``bcTools`` module into ``site-packages`` in your Python's installation library.

Alternatively, since ``bcTools`` is listed in the `Python Package Index <http://pypi.python.org/pypi/bcTools>`_ (PyPI), you can install it using your favorite Python packaging/distribution tool, for example with::

    > pip install bcTools

It's recommended to run ``_build_tables.py`` in the ``bcTools`` code directory after installation to make sure the parsing tables are pre-generated. This can make your code run faster.

Package contents
================

Once you unzip the ``bcTools`` package, you'll see the following files and directories:

README.rst:
  This README file.

setup.py:
  Installation script

bcTools/:
  The ``bcTools`` module source code.

tests/:
  Unit tests.

Contributors
============

`Barish Chandran B <http://www.barishcb.com>`_
