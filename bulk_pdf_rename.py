import os, shutil
from datetime import date
from os import walk

#this is a script that handles renaming pdfs, if you have a group of pdfs that need to be copied and renamed for multiple folders
#basically the files stay the same but you need multiple copies of them in different spots

#Set path
mypath = r'C:\Users\jk\OneDrive\Documents'

#Get files to rename
_, _, filesnames = next(walk(mypath))

#files will be copied into folders Sam and Dave
list = ['Sam','Dave']

today = date.today().strftime("%m_%d_%y")

for name in list:
    #this creates the new folders
    newdir = name + '_' + today + 'whatever'
    path = os.path.join(mypath,newdir)
    os.mkdir(path)

    #this copies the files
    for file in filenames:
        shutil.copy(mypath + '\\' + file,path)
        os.rename(path +'\\' + file,path + '\\' + name + file)