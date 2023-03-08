import pandas as pd
import numpy as np
import os,glob
from PIL import Image

path='C:/Users/duong/Documents/code/python/straug/test/'
dic='C:/Users/duong/Documents/code/python/straug/New folder'
with os.scandir(dic) as entries:
	for entry in entries:
		for file_name in glob.glob(os.path.join(dic+'/'+entry.name,'*.png')):
			img=Image.open(file_name)
			name=os.path.basename(file_name)
			loc=path+name.split('.')[0].split('/')[-1]+'_'+entry.name+'.png'
			print(loc)
			img.save(loc)  