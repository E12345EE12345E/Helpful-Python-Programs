##################################################
# This program should be downloaded into one of your existing file directories.
# Once there, import the functions below to start cleaning data.
# This is meant for people importing documents with additional formatting they want to remove before using the data.
# The first function writes data in a file.
# The second function returns the data.
# The third function combines them to cleanse the data, since .txt files don't have formatting.
# Enjoy!
##################################################

def pasteToNotepad(pasteLocation,data):
    with open(pasteLocation,"w") as file:
        file.write(data)
def copyToProgram(copyLocation):
    with open(copyLocation,"r") as file:
        return file.read()
def cleanse(location,data):
    with open(location,"w+") as file:
        file.write(data)
        return file.read()
