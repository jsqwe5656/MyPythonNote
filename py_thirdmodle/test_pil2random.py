# -*- coding: utf-8 -*-

from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

#生成随机zimu
def radChar():
    return chr(random.randint(65,90))

#生成随机颜色1
def radColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

#生成随机颜色2
def radColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

#设置图片宽高
width = 60*4
height = 60
image = Image.new('RGB',(width,height),(255,255,255))
#创建font对象
font = ImageFont.truetype('C:/windows/Fonts/Arial.ttf',36)
#创建Drwa对象
draw = ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=radColor())
#输出文字
for t in range(4):
    draw.text((60*t+10,10),radChar(),font=font,fill=radColor2())
#添加模糊效果
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')






