// strip.shift()
input.onButtonPressed(Button.A, function () {
    // strip.show_color(neopixel.colors(NeoPixelColors.RED))
    strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
    strip.show()
})
input.onGesture(Gesture.TiltLeft, function () {
	
})
input.onButtonPressed(Button.B, function () {
    // strip.show_color(neopixel.colors(NeoPixelColors.BLUE))-
    strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Blue))
    strip.show()
})
let strip: neopixel.Strip = null
strip = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
basic.forever(function () {
    strip.shift(0)
    basic.pause(30)
    strip.show()
})
