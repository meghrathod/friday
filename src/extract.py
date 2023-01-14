from zipfile import ZipFile


def extractAndList(filepath, probNumber):
    all_files = []
    with ZipFile(filepath, 'r') as zipObj:
        file_names = zipObj.namelist()
        if probNumber:
            for file in file_names:
                if file.startswith(probNumber) and file.endswith('.c'):
                    zipObj.extract(file, filepath[:len(filepath) - 4])
                    all_files.append(file)
        else:
            for file in file_names:
                if file.endswith('.c'):
                    zipObj.extract(file, filepath[:len(filepath) - 4])
                    all_files.append(file)
    return all_files
