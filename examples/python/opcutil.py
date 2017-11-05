import math

def even_spread(colors, num_leds):
    """Evenly spreads out the colors across the LEDs in order."""
    pixels = []
    pixels_per_color = math.floor(num_leds / len(colors))
    remainder = num_leds % len(colors)

    for color in colors:
        pixels += [color] * pixels_per_color
    pixels += [colors[0]] * remainder

    return pixels


def spread(colors, num_leds, pixels_per_color):
    """Spreads out the colors across the LEDs in order using the
    specified number of pixels per color."""
    pixels = []

    color_index = 0
    leds_left = num_leds
    while leds_left > 0:
        pixels += [colors[color_index]] * pixels_per_color
        color_index = (color_index + 1) % len(colors)
        leds_left -= pixels_per_color

    return pixels


def rotate_left(pixels):
    """Rotates the pixels to the left by one."""
    return pixels[1:] + pixels[:1]


def rotate_right(pixels):
    """Rotates the pixels to the right by one."""
    return pixels[-1:] + pixels[:-1]
