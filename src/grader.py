import csv
import json


def get_stu_name(filename,fileExtension):
    extensionLen= len(fileExtension)
    return filename.split('_')[-1][:-1*extensionLen]


def addMarks(fileNames, outPath, testPassList, testCasePath, bScore,fileExtension):
    with open(testCasePath, "r") as jfile:
        data = json.load(jfile)

    allMarks = []
    j = 0
    for student in testPassList:
        i = 0
        totalMarks = 0
        for inData in data["test_cases"]:
            totalMarks = totalMarks + (testPassList[j][i] * inData["marks"])
            i += 1
        allMarks.append(totalMarks)
        j += 1

    with open(outPath, 'w') as file:
        writer = csv.writer(file)

        if bScore:
            writer.writerow(["RollNo.", "TestCaseScore", "TimeScore"])
            for k in range(len(fileNames)):
                writer.writerow([get_stu_name(fileNames[k],fileExtension), allMarks[k], bScore[k]])
        else:
            writer.writerow(["RollNo.", "TestCaseScore"])
            for k in range(len(fileNames)):
                # print(get_stu_name(fileNames[k],fileExtension))
                writer.writerow([get_stu_name(fileNames[k],fileExtension), allMarks[k]])
    return 0
