import argparse
import os
from extract import extractAndList
from inio import takeio

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Main arg parser')
    parser.add_argument('-i', '--input-path', type=str, dest='zippath',
                        required=True, help='input path for the zip')
    parser.add_argument('-ti', '--test-input-path', type=str, dest='tipath',
                        required=True, help='input path for the zip')
    parser.add_argument('-to', '--test-output-path', type=str, dest='topath',
                        required=True, help='input path for the zip')
    parser.add_argument('-o', '--output-path', type=str, dest='outputpath',
                        required=False, help='output path for the extraction')

    args = parser.parse_args()

    if not os.path.isfile(args.zippath):
        raise ValueError("File doesn't exist")
    if not os.path.isfile(args.tipath):
        raise ValueError("File doesn't exist")
    if not os.path.isfile(args.topath):
        raise ValueError("File doesn't exist")

    zip_dir=args.zippath
    all_files = extractAndList(zip_dir)
    files_dir = zip_dir[:len(zip_dir) - 4] + '/'
    testCases=takeio(args.tipath)
    expOutput=takeio(args.topath)

    print(expOutput)


