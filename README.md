# jm_NeoAnim
Python scripts to convert a PNG file to an array of hex values suitable for animating NeoPixels

An augmentaton of [Neo Anim Project](https://learn.adafruit.com/circuit-playground-neoanim-using-bitmaps-to-animate-neopixels?view=all), that includes 8-bit per channel color for both RGB and RGBW arrays.

In order to convert neoAnim.png to a neoAnim.h file, you'll need to follow these steps:

1. Install [Python 3.5](https://www.python.org/downloads/)

2. Add the Pillow or [PIL imaging library](http://pillow.readthedocs.io/en/3.0.x/installation.html) to Python

3. Open a command shell and navigate to the where you saved the neoAnim.png file in your Arduino project sketch directory

4. Type the command to convert the bitmap to an RGB array: python convert2RGB.py neoAnim.png > neoAnim.h

  OR type the command to convert the bitmap to an RGBW array: python convert2RGB.py neoAnim.png > neoAnim.h

