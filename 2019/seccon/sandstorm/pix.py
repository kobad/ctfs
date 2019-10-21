from PIL import Image
import sys
import binascii
import struct

im = Image.open(sys.argv[1])
bands = ''.join(im.getbands())
width, height = im.size
pre=''
tr = ''
tg = ''
tb = '' 
ta = ''
t = ''

print(height)
print(width)


for h in range(height):
  for w in range(width):
    pixels = im.getpixel((w,h))

'''
for h in range(height):
  for w in range(width):
    pixels = im.getpixel((w,h))
    if bands == 'RGBA':
      r,g,b,a = pixels
      if r == 0:
        t += "0"
      else:
        t += "1"

      if g == 0:
        t += "0"
      else:
        t += "1"

      if b == 0:
        t += "0"
      else:
        t += "1"

      if a == 0:
        t += "0"
      else:
        t += "1"
    else:
      print("-----------")
      break
'''

# print((eval("0b"+t)))
