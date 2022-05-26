import os
for folderName, subfolders, filenames in os.walk('C:\\users'):
    print('The folder is ' + folderName)
    print('the subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('the filenames in ' + folderName + ' are: ' + str(filenames))
    print()