import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# Define your GPIO pins - adjust these to match your actual wiring
keyboard.col_pins = (board.P0_09, board.P0_10)
keyboard.row_pins = (board.P1_15, board.P1_14, board.P1_13)  # Empty since you're not using a matrix

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Define your keymap - one layer with 4 keys
keyboard.keymap = [
    [KC.MUTE, KC.VOLU, KC.VOLD, KC.MPLY, KC.COPY, KC.PASTE]  # Replace with whatever keys you want
]

if __name__ == '__main__':
    keyboard.go()
