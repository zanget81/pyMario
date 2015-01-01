pyMario
=======

An amateur port to PC written in Python of the Super Mario Bros for NES. 

Requirements
------------

python (2.7):

        https://www.python.org/downloads/

Tests
-----

    nosetests --with-coverage --cover-package=.

    with standard output:

    nosetests --with-coverage --nocapture --cover-package=.

Run
---
    python -m src.main



Release process
---------------

Windows
-------

Using py2exe:

    python setup.py py2exe

    (Currently not working)