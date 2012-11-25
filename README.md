This project is an implementation of the Chip 8 system emulator written on Python.

Documentation can be found at:

http://www.multigesture.net/articles/how-to-write-an-emulator-chip-8-interpreter/

Chip8System Class
-----------------

This class implements the chip-8 system.  Methods provide functionality for initialization and entry into the
emulation cycle.

e.g. ::

    >>> import chip_8
    >>> system = chip_8.Chip8System()
    >>> system.initialize()
    >>> system.emulate_cycle()