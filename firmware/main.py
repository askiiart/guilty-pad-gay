# import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# Define your GPIO pins - adjust these to match your actual wiring
keyboard.col_pins = ('GP2', 'GP4', 'GP3', 'GP6')
keyboard.row_pins = ()  # Empty since you're not using a matrix

# Since there's no matrix, set this to COLUMNS
keyboard.diode_orientation = DiodeOrientation.COLUMNS

# Define your keymap - one layer with 4 keys
keyboard.keymap = [
    [KC.MUTE, KC.VOLU, KC.VOLD, KC.MPLY]  # Replace with whatever keys you want
]

if __name__ == '__main__':
    keyboard.go()