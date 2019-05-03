import os
import shutil
import zipfile 

print("..........................................")
print("\n")
print("Welcome To The All in One File Operation Script ....")
print("\n")
print("..........................................")
print("\n")

print("Your Current Working Directory Is "+ os.getcwd() )
print("\n")

theDir = os.getcwd()

ans = input("Do You Want To Change The Working Directory ? (Y/N) \n ")

yes = {"y", "Y", "Yes", "yes", "YES"}
no = {"n", "N", "No", "NO"}

if ans in yes:
    theDir = input("Enter The Directory Path: ")
if ans in no:
    print("Working Directory Not Changed....")

print("\n")


fileExt = input("Type The File Extension You Want To Filter: \n")
print("\n")
print("Files With " + fileExt + " Extensions are : \n")
print("\n")

speFile = []

for roots, dirs, files in os.walk(theDir):
    for file in files:
        if file.endswith(fileExt):
            speFile.append(file)

print("\n")
print("Files With " + fileExt + " Extensions are : \n")
print(speFile)
print("\n")

def backupFiles():
    print("\n")
    desPath = input("Paste The Destination Path where You Want To BackUp The Files : \n ")

    for item in speFile:
        shutil.copy(theDir+"\\"+item, desPath)
        print("File Copied SuccessFully..")


def deleteFiles():
    deleteConfirmation = input("Do You To Want To Delete all File With " + fileExt + " Extension (Y/N) \n")


    if deleteConfirmation in yes:
        for item in speFile:
            send2trash.send2trash(theDir+"\\"+item)
            print("Deleting Files.......")
    if deleteConfirmation in no:
        print("Files Not Deleted...........")

def archiveFiles():
    os.chdir(theDir)
    newZip = zipfile.ZipFile("New.zip", "w")
    for item in speFile:
        newZip.write(item, compress_type = zipfile.ZIP_DEFLATED)
        print("Archiving")
    newZip.close()


print("\n")
print("Enter 1 For backup The File To a Specific location....")
print("Enter 2 For Deleting The Files....")
print("Enter 3 For Archive The FIles Into Zip.......")
choice = input("Enter Your Choice :")

if (choice is "1"):
	backupFiles()

if (choice is "2"):
	deleteFiles()

if (choice is "3"):
	archiveFiles()