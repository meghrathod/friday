import shutil


def removeAllExtracted(folderPath):
    try:
        shutil.rmtree(folderPath)
        print("Removed Folder Successfully")
    except OSError as error:
        print(error)
