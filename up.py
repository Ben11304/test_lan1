from straug.noise import GaussianNoise
from straug.noise import ShotNoise
from straug.noise import ImpulseNoise
from straug.noise import SpeckleNoise
import cv2,os,glob
from PIL import Image
import pathlib
import pandas as pd
import numpy as np
def aug(img,op,out_path):
        im_arr = np.array(img)
        Y, X = np.where(np.all(im_arr!=[255,255,255],axis=2))
        for i in range(len(Y)):
            im_arr[Y[i]][X[i]]=[255,0,0]
        img = Image.fromarray(im_arr)        
        im = op()(img,mag=0)
        im_arr = np.array(im)
        Y, X = np.where(np.all(im_arr!=[255,255,255],axis=2))
        for i in range(len(Y)):
            im_arr[Y[i]][X[i]]=[255,255,255]
        im = Image.fromarray(im_arr).convert("L")
        save_path = out_path+ '/' + str(op).split('.')[2].split("'")[0]
        
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        im.save(os.path.join(save_path,pathlib.Path(file_name).stem + '.png'))         
        return im

y=[]
out_path='C:\\Users\\duong\\Documents\\code\\python\\CROHM23\\img_last'
dic = 'C:\\Users\\duong\\Documents\\code\\python\\CROHM23\\Img'
for file_name in glob.glob(os.path.join(dic+'/'+'*.png')):
	im=Image.open(file_name).convert('RGB')
	aug(im,GaussianNoise,out_path+'\\Gaussian')


