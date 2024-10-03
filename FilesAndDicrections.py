from pathlib import Path


#we can use an absolute path or relative path

#in the Absolute path we start from the root of our hardisk
#example c:\Program Files\Microsoft\Windows\CurrentVersion
#/usr/local/bin/python

#relative path we can just use the name of the folder



path = Path("Package2")
print(path.exists())


#we can also make directory using the same code above
#   path = Path("NewDirectory")
#   path.mkdir() For making directory
#   path.rmdir() For removing directory
#   path.glob('Package2') to search for a directory
#   path.glob('*.*') to show all directories
#   path.glob('*.py') to show all directories that is with the extinsion .py (we have to use for loop)