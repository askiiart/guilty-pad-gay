# magnetopad

little macropad with a screen and leds. gonna magnetically attach to a keyboard (to come later) which will communicate with it via pogo pins.

## parts not in the kicad file
- pogo pins: https://www.alibaba.com/product-detail/4-pin-Bent-Magnetic-Connector-Male_1601395017888.html

## parts in the kicad file
- 2x 1N4001 diodes
- 1x XIAO RP2040
- 4x SK6812 MINI
- keyboard switches with clear bits for backlights

## notes

the side LEDs are on a separate board (attached by mouse bites), and you need to solder a few wires between the two boards. it's then to be mounted above the rp2040
