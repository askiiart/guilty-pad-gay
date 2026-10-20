import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# define GPIO pins - probably different irl but not gonna break out micropython atm just to check
keyboard.col_pins = (board.P0_09, board.P0_10)
keyboard.row_pins = (board.P1_15, board.P1_14, board.P1_13)  # empty since not using a matrix

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# define keymap
keyboard.keymap = [
    [KC.MUTE, KC.VOLU, KC.VOLD, KC.MPLY, KC.COPY, KC.PASTE]
]

if __name__ == '__main__':
    keyboard.go()
