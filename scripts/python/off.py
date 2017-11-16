import opc

numLEDs = 512
client = opc.Client('localhost:7890')

black = [(0,0,0)] * numLEDs

client.put_pixels(black)
