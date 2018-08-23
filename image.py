import os
import matplotlib.pyplot as plt
import matplotlib.image as mping

train_dir=os.path.join('/home/krithick/Desktop/hari/Hariharan/training ')
validate_dir= os.path.join('/home/krithick/Desktop/hari/Hariharan/validate')

train = os.listdir(train_dir)
validate = os.listdir(validate_dir)

fname1 = [os.path.join(train_dir,fname)
        for fname in train[:]]

fname2 = [os.path.join(validate_dir,fname)
        for fname in validate[:]]
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
plt.show()
