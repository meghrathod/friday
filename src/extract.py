from zipfile import ZipFile

def extractAndList(filepath):
    with ZipFile(filepath, 'r') as zipObj:
        zipObj.extractall(filepath[:len(filepath)-4])
        all_files = zipObj.namelist()
    return all_files
