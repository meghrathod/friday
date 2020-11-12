from zipfile import ZipFile

def extractAndList(filepath,probNumber):
    all_files=[]
    with ZipFile(filepath, 'r') as zipObj:
        if probNumber:
            file_names=zipObj.namelist()
            for file in file_names:
                if file.startswith(probNumber):
                    zipObj.extract(file,filepath[:len(filepath)-4])
                    all_files.append(file)
        else:
            zipObj.extractall(filepath[:len(filepath)-4])
            all_files = zipObj.namelist()
    return all_files
