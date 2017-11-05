import math

def even_spread(colors, numLEDs):
    """Evenly spreads out the colors across the LEDs in order"""
    pixels = []
    pixels_per_color = math.floor(numLEDs / len(colors))
    remainder = numLEDs % len(colors)

    for color in colors:
        pixels += [color] * pixels_per_color
    pixels += [colors[0]] * remainder

    return pixels
