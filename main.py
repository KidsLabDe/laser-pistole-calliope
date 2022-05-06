# strip.shift()

def on_button_pressed_a():
    # strip.show_color(neopixel.colors(NeoPixelColors.RED))
    strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
    strip.show()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    pass
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

# 

def on_button_pressed_b():
    # strip.show_color(neopixel.colors(NeoPixelColors.BLUE))-
    strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLUE))
    strip.show()

input.on_button_pressed(Button.B, on_button_pressed_b)

strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)

def on_forever():
    strip.shift()
    basic.pause(30)
    strip.show()

basic.forever(on_forever)
