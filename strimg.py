from PIL import Image
import sys

def encode ():
	im = Image.open(sys.argv[2]).convert("RGB") # Convert to RGB in case of alpha channel
	encoded = ""
	for x in range(im.size[0]):
		for y in range(im.size[1]):
			pxl = im.getpixel((x,y))
			encoded += chr(pxl[0]) + chr(pxl[1]) + chr(pxl[2]) # Get character for R/G/B 0-255 value
	encoded += chr(im.size[0]) + chr(im.size[1]) # Last two characters encode image size
	with open("out","w") as o: o.write(encoded) # Export all values to out file

def decode ():
	with open(sys.argv[2],"r") as dat: data = dat.read()
	size = [ord(data[-2]),ord(data[-1])] # Read back image size
	newIm = Image.new("RGB",(size[0],size[1])) # Make a new image with size
	for x in range(size[0]):
		for y in range(size[1]):
			idx = 3 * (x * size[1] + y) # Each pixel is 3 characters, get every 3rd index
			newIm.putpixel((x,y),(ord(data[idx]),ord(data[idx+1]),ord(data[idx+2]))) # Get value for character
	newIm.show()

encode() if sys.argv[1] == "-e" else decode()