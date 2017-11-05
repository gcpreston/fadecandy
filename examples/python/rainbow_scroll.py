import opc
import opcutil
import time

client = opc.Client('localhost:7890')

num_leds = 60
colors = [(255, 0, 0),  # red
          (255, 127, 0),  # orange
          (255, 255, 0, 0),  # yellow
          (0, 255, 0),  # green
          (0, 0, 255),  # blue
          (139, 0, 255)]  # violet
pixels = opcutil.even_spread(colors, num_leds)

while True:
    client.put_pixels(pixels)
    time.sleep(0.1)
    pixels = rotate_right(pixels)
