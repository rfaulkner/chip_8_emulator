
__author__ = 'rfaulkner'
__date__ = '11/17/12'
__license__ = "GPL (version 2 or later)"

class Chip8System(object):
    """
        This class emulates a Chip-8 system.

        0x000-0x1FF - Chip 8 interpreter (contains font set in emu)
        0x050-0x0A0 - Used for the built in 4x5 pixel font set (0-F)
        0x200-0xFFF - Program ROM and work RAM
    """

    __opcode = 0x00             # stores a single opcode
    __memory = [0x0] * 4096     # system memory
    __V = [0x00] * 16           # system registers
    __I = 0x000                 # index pointer
    __PC = 0x000                # program counter
    __gfx = [0b0] * (64 * 32)   # graphics bit array
    __delay_timer = 0x0         # timer register
    __sound_timer = 0x0         # timer register
    __stack = [0x0] * 16        # stack
    __sp = 0x0                  # stack pointer
    __key = [0x0] * 16          # system keypad state

    def __init__(self, *args, **kwargs):
        super(Chip8System, self).__init__()

    def __new__(cls, *args, **kwargs):
        return super(Chip8System, cls).__new__(cls, *args, **kwargs)

    def __del__(self): raise NotImplementedError

    def __doc__(self): return super(Chip8System, self).__doc__

    def __setitem__(self, key, value): raise NotImplementedError
    def __getitem__(self, item): raise NotImplementedError

    def game_loop(self): raise NotImplementedError

def main(): raise NotImplementedError

if __name__ == '__main__':
    main()

