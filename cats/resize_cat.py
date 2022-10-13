# FILE NO # 2A
# in this file we resize the cats pictures , convert them into gray scale ,
# then renaming them and save them into a folder
from PIL import Image
import glob
import os

lst_imgs = [i for i in glob.glob("*.png")] # we Itrate throughout the png pics in the folder given

if not "ltl" in os.listdir(): # if there is no file called ltl
	os.mkdir("ltl")          # It creates a folder called ltl if does't exist

k = 1 						# varible to start renaming the pics in the folder
for i in lst_imgs:
	img = Image.open(i)
	img = img.resize((64, 64), Image.ANTIALIAS) # resize command
	img = img.convert('L')    					# convert to gray scale
	img.save("ltl\\" + str(k) + ".png")			# save using the K index given
	k = k +1									# increment the K index

os.startfile("ltl")  # open the ltl file we created
