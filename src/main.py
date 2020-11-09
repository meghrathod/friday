from extract import extractAndList

zip_dir=input("Please Enter the Directory of the zip containing all the Submissions :")
all_files=extractAndList(zip_dir)
files_dir=zip_dir[:len(zip_dir)-4]+'/'


