import argparse
import os
from extract import extractAndList
from inio import takeio
from testrunner import runTest
from grader import addMarks
from calcBonus import get_bonus_score


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Main arg parser')
    parser.add_argument('-i', '--input-path', type=str, dest='zippath',
                        required=True, help='input path for the zip')
    parser.add_argument('-ti', '--test-case-path', type=str, dest='testpath',
                        required=True, help='input path for the zip')
    parser.add_argument('-o', '--output-path', type=str, dest='outpath',
                        default='./testResults.csv', help='output path for the extraction')
    parser.add_argument('-r','--record-time',action='store_true',dest='checkTime',help='use to record runtime')

    args = parser.parse_args()

    if not os.path.isfile(args.zippath):
        raise ValueError("File(Zip Input) doesn't exist")
    if not os.path.isfile(args.testpath):
        raise ValueError("File(Test Case) doesn't exist")

    zip_dir=args.zippath
    all_files = extractAndList(zip_dir)
    files_dir = ".".join(zip_dir.split('.')[:-1])

    casesPassed=[]
    timetaken=[]

    for file in all_files:
        test_result, time = runTest(args.testpath,files_dir,file)
        casesPassed.append(test_result)
        if args.checkTime:
            timetaken.append(time)
    bScore=[]
    maxM=10 ##Figure out how to get max bonus
    if args.checkTime:
        bScore=get_bonus_score(timetaken,maxM)
    addMarks(all_files, args.outpath, casesPassed, args.testpath,bScore)




