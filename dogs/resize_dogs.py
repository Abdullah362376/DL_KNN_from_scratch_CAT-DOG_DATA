# FILE NO # 2B
# in this file we resize the dogs pictures , convert them into gray scale ,
# then renaming them and save them into a folder
from PIL import Image
import glob
import os

lst_imgs = [i for i in glob.glob("*.png")] # we Iterate throughout the png pics in the folder given
if not "doggy" in os.listdir():              # if there is no file called ltl
	os.mkdir("doggy") 						 # It creates a folder called doggy if does't exist

k = 1										# varible to start renaming the pics in the folder
for i in lst_imgs:
	img = Image.open(i)
	img = img.resize((64, 64), Image.ANTIALIAS) # resizing
	img = img.convert('L') 						# converting to gray scale
	img.save("doggy\\" + str(k) + ".png")		# save in base of the K index
	k = k +1									# increment the k index

os.startfile("doggy")							# show the folder doggy