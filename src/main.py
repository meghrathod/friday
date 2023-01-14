import argparse
import os
from extract import extractAndList
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
                        default='../testResults.csv', help='output path for the extraction')
    parser.add_argument('-r', '--record-time', action='store_true', dest='checkTime', help='use to record runtime')
    parser.add_argument('-m', '--max-bonus-score', type=int, dest='maxB',
                        default=10, help='maximum bonus score')
    parser.add_argument('-to', '--timeout', type=int, dest='timeOut',
                        default=60, help='set timeout for each testcase')
    # parser.add_argument('-cl', '--clang', action='store_true', dest='useClang', help='use clang instead of gcc')
    parser.add_argument('-lng', '--language', type=str, dest='language', required=True, help='Choose language to test')
    parser.add_argument('-pn', '--problem-num', type=str, dest='pname',
                        default='', help='use to specify a specific problem number')
    parser.add_argument('-ww', '--without-whitespace', action='store_true', dest='raWhitespaces',
                        help='comparison after removing all whitespaces from I/O')
    parser.add_argument('-abs', '--absolute-comparison', action='store_true', dest='kWhitespaces',
                        help='char by char comparison ')

    args = parser.parse_args()

    # if args.useClang:
    #     cname = 'clang'
    # else:
    #     cname = 'gcc'

    #cname = 'g++'
    match args.language:
        case "C":
            cname = 'gcc'
            fileExtension = '.c'
        case "Clang":
            cname = 'clang'
            fileExtension = '.c'
        case "CPP":
            cname = 'g++'
            fileExtension = '.cpp'

    #print(fileExtension)

    if args.raWhitespaces:
        compType = 'rAll'
    elif args.kWhitespaces:
        compType = 'abs'
    else:
        compType = 'part'

    if not os.path.isfile(args.zippath):
        raise ValueError("File(Zip Input) doesn't exist")
    if not os.path.isfile(args.testpath):
        raise ValueError("File(Test Case) doesn't exist")

    zip_dir = args.zippath
    #print(zip_dir)
    all_files = extractAndList(zip_dir, args.pname, fileExtension)
    files_dir = ".".join(zip_dir.split('.')[:-1])
    #print(files_dir)
    #print(all_files)

    casesPassed = []
    timetaken = []

    #print("Reaches Call")

    for file in all_files:
        #print("Gets inside loop")
        test_result, time = runTest(args.testpath, files_dir, file, args.timeOut, cname, compType)
        #print(test_result)
        #print(time)
        casesPassed.append(test_result)
        if args.checkTime:
            timetaken.append(time)
    bScore = []

    if args.checkTime:
        bScore = get_bonus_score(timetaken, args.maxB)
    addMarks(all_files, args.outpath, casesPassed, args.testpath, bScore,fileExtension)
