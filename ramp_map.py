from PIL import Image

ramp = Image.new('RGB', (256, 256))  # Default color = black
(width, height) = ramp.size

ramp_map = ramp.load()

for y in range (height):
    for x in range (width):
            ramp_map[x, y] = x, y , ((x + y) // 2)
               
ramp.save("color_ramp.png")
