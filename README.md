# how-to-read-a-multiple-images-from-folder-using-matplotlip-in-python.

This a my fun time project. This is help to read a multiple images from your local system. Matplotlib is a python library function it help to read a multiple file. 

# Install matplotlib (only ubuntu)

  # Ubuntu
  
  sudo apt-get update
  
  python3 -mpip install -U pip
  
  python3 -mpip install -U matplotlib  


# Code explain

import os # to access a system file


import matplotlib.pyplot as plt
import matplotlib.image as mping      # import a matplotlib



in = os.listdir(train_dir)
validate = os.listdir(validate_dir)

fname1 = [os.path.join(train_dir,fname)
        for fname in train[:]]

fname2 = [os.path.join(validate_dir,fname)
        for fname in validate[:]]             # read a multiple image file name from the foldre
        
        

ncolu = 4
nrow = 4
fig = plt.gcf()
fig.set_size_inches(ncolu*4,nrow*4)
for i,fname in enumerate(fname1):
    print (fname)
    sp = plt.subplot(4,5,i+1)
    sp.axis('off')
    img = mping.imread(fname)
    plt.imshow(img)
plt.show()                                # To display the multiple images.
