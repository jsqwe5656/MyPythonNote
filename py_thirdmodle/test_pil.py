# -*- coding: utf -8 -*-

from PIL import Image,ImageFilter

#打开一个jpg图像文件，若非当前路径请指定路径
im = Image.open('test.jpg')
#获取图像尺寸
w,h = im.size
print('%s,%s' % (w,h))
#缩放到50%
im.thumbnail((w//2,h//2))
print('%s,%s'%(w//2,h//2))
#将缩放后的图片以jpeg的格式保存到当前路径
im.save('thumbnail.jpg','jpeg')

im2 = Image.open('thumbnail.jpg')
#应用模糊滤镜
im3 = im2.filter(ImageFilter.BLUR)
im3.save('blur.jpg','jpeg')
