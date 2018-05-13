'''
This tool is used for labeling images , it reads all the images inside a folder and displays them
one by one,so the user can label them .

Author Rabee A. Kiblawi --12-5-2018
'''

import cv2
import os 


#put your own path below 
PATH = r'E:\workspace\python_workSpace\capture1'

os.chdir(PATH)

num_classes =  int(input('enter number of classes'))

names = [] #class names
keys = [] #keycodes

for i in range(0,num_classes):
     name =  input('enter name of class '+str(i))
     names.append(name)
     try:
         os.mkdir(PATH+r'\\'+name)
     except OSError as e:
         print(str(e))
     finally:
         pass
     key = input('enter a char key ,to press when labeling')
     keys.append(key)
     

files = os.listdir(PATH)

 
for file in files :
    #you can add more ext below
    if file.endswith('.jpg') or file.endswith('.png') : 
        img = cv2.imread(file)
        cv2.imshow('image',img)
        key = cv2.waitKey(0) #& 0xFF
        for k in keys:
            if key == ord(k):
                path =PATH +r'\\'+names[keys.index(k)]+r'\\'
                img_indx = len(os.listdir(path))#count images in dest folder
                cv2.imwrite(path+str(img_indx)+'.jpg',img)
                os.remove(file)
            
cv2.destroyAllWindows()