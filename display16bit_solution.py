import matplotlib as mpl 
mpl.rc('image', cmap='gray') 
import matplotlib.pyplot as plt
import cv2
import numpy as np

# read input image file
img = cv2.imread('composite_monosm.tif',-1);

# max. value for 16bit (uint16) 
b16 = 2**16 -1; #65535

# normalize input image to range [0,1] 
img = np.double(img)/b16;


# use different display ranges 
plt.subplot(2,2,1); 
plt.imshow(img); # range [0,1] 
plt.title('full range');

plt.subplot(2,2,3); 
plt.imshow(img,vmax=0.25);# [0,0.25] 
plt.title('low range');

plt.subplot(2,2,4); 
sc = 0.1; # range [0.1, 1] 
plt.imshow(img, vmin=0.1); 
plt.title('high range');


"""
plt.figure()
# use different display ranges
plt.subplot(2,2,1);
plt.imshow(img);   # range [0,1]
plt.title('full range');
 
#display low range (0-16383.75)
plt.subplot(2,2,3);
high=16383
plt.imshow(img, vmax=high/16);  # range [0,0.25]
plt.title('low range');

#display mid range (255-6000)
plt.subplot(2,2,4);
low=255
high=6000
sc = 0.1; #range [0.1, 1]
plt.imshow((img-sc)/(1-sc)); 
plt.title('mid range');
"""
#plt.colormap(cv2.gray);