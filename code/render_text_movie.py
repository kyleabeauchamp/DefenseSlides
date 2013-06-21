import ImageFont, ImageDraw
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf", 60)
dt = 100. / 10000.

for i in range(1,10001):
    print(i)
    image = Image.open("old_png/frame%.4d.png" % i)
    timestep = (i - 1.) * dt
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), u"%04.1fμs" % timestep, font=font, fill="black")
    image.save("png/frame%.4d.png" % i)
