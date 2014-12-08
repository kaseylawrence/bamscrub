__author__ = 'kasey'
import os, glob

#set folder name to current working directory.
folder_name = os.curdir
bam_file = os.path.join(folder_name, '*.bam')
#Look for bam files that do not have "sorted" in the file name
for file in glob.glob(bam_file):
    if "sorted" not in file:
        os.remove(file)
        print "removed", file
    else:
        pass
        
